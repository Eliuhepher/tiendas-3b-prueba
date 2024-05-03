# Prueba Técnica Tiendas 3B por Eliu Hepher G.

Para la ejecución del proyecto se requiere tener Docker instalado.

## 1. Clonar el repositorio.
- Ejecutar en su equipo local con git instalado ``` git clone https://github.com/Eliuhepher/tiendas-3b-prueba ```
- Una vez descargado, posicionarse dentro de la carpeta "tiendas-3b-prueba"
![image](https://github.com/Eliuhepher/tiendas-3b-prueba/assets/70795995/169cf5bc-3eba-47fb-a72c-2f372da98fb8)

## 2. Ejecución. 
* Antes de iniciar la ejecución asegúrese que Docker se encuentra ejecutando de manera correcta con ``` docker info```
1. Abra una terminal de su preferencia (cmd, PowerShell, bash, etc) y ejecute el comando ```docker compose build```. Este comando construirá las imágenes de los servicios definidos en el archivo ```docker-compose.yml```
   Nota: Si utiliza la terminar de Powershell en Windows, puede requerir modificar las politicas de ejecución. Vea más en [Documentación de Microsoft acerca de Powershell](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.4)
3. En la misma terminal ejecute ```docker compose up```. Este comando pondrá en ejecución los servicios construidos previamente.
   Como salida observará la aplicación de migraciones y el resultado de las pruebas unitarias.
   ![image](https://github.com/Eliuhepher/tiendas-3b-prueba/assets/70795995/e95d43ce-117b-4042-b764-1cdecb7a3fac)

   Al final, debe observar que la aplicación inicia correctamente en la dirección ``` http://0.0.0.0:8000/ ```

   ![image](https://github.com/Eliuhepher/tiendas-3b-prueba/assets/70795995/bf796566-e1f3-4106-9b76-bd7510e5d945)

   Nota: Si llegase a tener problema con la ejecución, puede probar purgando las imagenes actuales con el comando ```docker system prune```

   ![image](https://github.com/Eliuhepher/tiendas-3b-prueba/assets/70795995/7bec318a-87c1-40d5-8744-92b41da1cbc8)

## 3. Interacción.
- Refiérase a la siguiente documentación para comenzar a enviar peticiones
- [Link a Documentación en Postman](https://documenter.getpostman.com/view/9987438/2sA3JFCQSR#intro)

  ![image](https://github.com/Eliuhepher/tiendas-3b-prueba/assets/70795995/597ee280-2593-4e68-8067-dd72ccac1d67)

  


