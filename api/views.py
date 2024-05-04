from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
)

from .serializers import (
    ProductRequestSerializer,
    ProductResponseSerializer,
    ProductPatchSerializer,
)

from .models import Product


class ProductView(APIView):
    """
    Views to handle Product requests
    """

    def get(self, _request, sku=None):

        if sku:
            try:
                product = Product.objects.get(sku=sku)
                serializer = ProductResponseSerializer(product)
            except Product.DoesNotExist as error:
                return Response(
                    {"error": True, "message": error}, status=HTTP_400_BAD_REQUEST
                )

        else:
            products = Product.objects.all()
            serializer = ProductResponseSerializer(products, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    def post(self, request):
        serializer = ProductRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def patch(self, request, sku=None):

        if request.data.get("stock"):
            updated_stock = request.data.get("stock")
            try:
                product_to_update = Product.objects.get(sku=sku)
            except Product.DoesNotExist as error:
                return Response(
                    data={"error": True, "message": f"{error}"},
                    status=HTTP_404_NOT_FOUND,
                )

            serializer = ProductPatchSerializer(
                product_to_update,
                data={"stock": product_to_update.stock + updated_stock},
                partial=True,
            )
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, HTTP_200_OK)
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        else:
            return Response(
                data={
                    "message": "The field 'stock' is required in request body",
                    "error": True,
                },
                status=HTTP_400_BAD_REQUEST,
            )


class OrderView(APIView):

    def post(self, request):
        data = request.data
        all_have_stock = []

        for element in data:
            sku = element.get("sku")
            purchase = element.get("quantity")
            all_have_stock.append(
                True if purchase <= Product.objects.get(sku=sku).stock else False
            )

        if all(all_have_stock):
            for element in data:

                sku = element.get("sku")
                purchase = element.get("quantity")

                product_to_update = Product.objects.get(sku=sku)
                if product_to_update.stock <= 10:
                    print(f"¡Atención! El producto {product_to_update.sku} | {product_to_update.name} está próximo a agotarse. Su stock actual es de {product_to_update.stock}")
                product_to_update.stock = product_to_update.stock - purchase
                product_to_update.save()

                
            return Response(
                data={"message": "Compra realizada con éxito", "error": False},
                status=HTTP_200_OK,
            )

        else:
            return Response(
                data={"message": "No se pudo concretar la compra", "error": False},
                status=HTTP_400_BAD_REQUEST,
            )
