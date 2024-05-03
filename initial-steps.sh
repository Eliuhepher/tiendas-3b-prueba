#!/bin/sh
echo "Creando migraciones"
python manage.py makemigrations
echo ====================================

echo "Aplicando migraciones"
python manage.py migrate
echo ====================================

echo "Ejecutando pruebas unitarias"
python manage.py test
echo ====================================

echo "Iniciando servicio"
python manage.py runserver 0.0.0.0:8000