FROM python:3.11-alpine
ENV PYTHONUNBUFFERED=1
RUN mkdir /Tiendas3B
WORKDIR /Tiendas3B
COPY requirements.txt /Tiendas3B/
RUN pip install -r requirements.txt
COPY initial-steps.sh /Tiendas3B/
EXPOSE 8000
COPY . /Tiendas3B/
ENTRYPOINT [ "/Tiendas3B/initial-steps.sh" ]
#CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]