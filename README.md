Instrucciones para la Configuración del Proyecto Django
Bienvenidos al proyecto Django. Para configurar y utilizar este proyecto en su computadora local, sigan los siguientes pasos detalladamente:
1. Crear una Carpeta de Trabajo: Inicie creando una carpeta en su computadora donde alojará el proyecto.
2. Clonar el Repositorio: Abra la consola de comandos y navegue hasta la carpeta que ha creado. Ejecute el siguiente comando para clonar el repositorio:

   git clone https://github.com/criticalRobin/try_django_weasyprint.git
4. Preparación del Entorno Virtual: Antes de continuar, asegúrese de tener instalado Python y el gestor de paquetes pip. Puede verificar su instalación con los comandos python --version y pip --version.
5. Instalación de Virtualenv: Si no tiene virtualenv instalado, puede hacerlo mediante pip con el siguiente comando: pip install virtualenv
6. Creación del Entorno Virtual: Dentro de la carpeta del proyecto, cree un entorno virtual ejecutando: python -m venv env
7. Activación del Entorno Virtual: Antes de proceder con la instalación de dependencias y la configuración del proyecto, active el entorno virtual. En Windows, use: env\Scripts\activate
   En sistemas Unix o MacOS, use: source env/bin/activate
8. Instalación de Dependencias: Una vez activado el entorno virtual, instale las dependencias del proyecto ejecutando: pip install -r requirements.txt
9. Configuración Tailwind + Django: Una vez instaladas las dependencias siga los siguientes pasos para configurar Tailwind css:
    1. Abra el proyecto dentro de su editor de código preferido.
    2. En el directorio llamado change_forms abrir el documento settings.py
       ![image](https://github.com/criticalRobin/try_django_weasyprint/assets/133540422/f738bf55-242e-4cf3-91b9-9c19680ce470)

    3. Vaya a la sección de INSTALLED_APPS y comente las siguientes apps: theme y django_browser_reload
       ![image](https://github.com/criticalRobin/try_django_weasyprint/assets/133540422/18e68806-61c2-4f92-8c68-a4965ba52adc)

    4. Una vez comentadas esas aplicaciones ejecute el siguiente comando en su consola: python manage.py tailwind init
    5. Cuando le aparezca lo presentado en la imagen solo presione enter para continuar
      ![image](https://github.com/criticalRobin/try_django_weasyprint/assets/133540422/b1579ca3-b41b-4464-8b98-d0ef52b630a8)

    6. Una vez realizado eso le aparecerá un mensaje de que se ha creado la app theme dentro del proyecto, vaya de nuevo al archivo settings.py y descomente la app theme
      ![image](https://github.com/criticalRobin/try_django_weasyprint/assets/133540422/ef5230a5-7c2a-49a8-8646-ed510814ccfb)

    7. Vuelva a su consola y ejecute el siguiente comando: python manage.py tailwind install
    8. Una vez instaladas todas las dependencias de tailwind le aparecerá un mensaje como el de la imagen:
      ![image](https://github.com/criticalRobin/try_django_weasyprint/assets/133540422/830d89f4-85fb-437c-bee4-dd4be9216357)

    9. Vuelva al archivo settings.py y descomente en la sección de apps instaladas la app con el nombre: django_browser_reload
      ![image](https://github.com/criticalRobin/try_django_weasyprint/assets/133540422/02591896-bb05-4867-a681-d0cc9234e6b4)

    10. Para comprobar la correcta configuración ejecute el comando: python manage.py tailwind start
    11. Si todo salió bien deberia ver en su consola lo mismo que en la imagen a continuación:
      ![image](https://github.com/criticalRobin/try_django_weasyprint/assets/133540422/a2087ca3-b025-4cbf-b426-9234c28324c1)

11. Comprobación Dependencias: Ejecute el comando: python manage.py runserver
   ![image](https://github.com/criticalRobin/try_django_weasyprint/assets/133540422/b87c5d3c-65b3-4171-821d-86f6a0230478)
   Si obtiene un resultado como el de la imagen significa que los pasos anteriores fueron realizados con éxito.
12. Si en el paso anterior aparecieron errores relacionados con la libreria weasyprint, observe este video para usar weasyprint en youtube: https://www.youtube.com/watch?v=rtXLsf6Vfss&t=381s&ab_channel=AlgoriSoft

    Si es usuario de linux, más especificamente en Ubuntu ejecute el siguiente comando dentro de la consola: apt install python3-pip python3-cffi python3-brotli libpango-1.0-0 libharfbuzz0b libpangoft2-1.0-0

    De igual forma se adjunta la documentación de weasyprint: https://doc.courtbouillon.org/weasyprint/stable/index.html
13. Ejecutar Migraciones: Presione control+c para detener la ejecución de la app web, cuando se haya detenido ejecute el siguiente comando: python manage.py migrate
14. Crear Super Usuario: Finalmente ejecute el comando: python manage.py createsuperuser y complete el formulario de registro, con esto ya podrá acceder al admin view del proyecto de Django.
