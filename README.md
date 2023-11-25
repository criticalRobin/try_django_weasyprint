Instrucciones para la Configuración del Proyecto Django
Bienvenidos al proyecto Django. Para configurar y utilizar este proyecto en su computadora local, sigan los siguientes pasos detalladamente:
1. Crear una Carpeta de Trabajo: Inicie creando una carpeta en su computadora donde alojará el proyecto.
2. Clonar el Repositorio: Abra la consola de comandos y navegue hasta la carpeta que ha creado. Ejecute el siguiente comando para clonar el repositorio:
   git clone https://github.com/criticalRobin/try_django_weasyprint.git
3. Preparación del Entorno Virtual: Antes de continuar, asegúrese de tener instalado Python y el gestor de paquetes pip. Puede verificar su instalación con los comandos python --version y pip --version.
4. Instalación de Virtualenv: Si no tiene virtualenv instalado, puede hacerlo mediante pip con el siguiente comando: pip install virtualenv
5. Creación del Entorno Virtual: Dentro de la carpeta del proyecto, cree un entorno virtual ejecutando: python -m venv env
6. Activación del Entorno Virtual: Antes de proceder con la instalación de dependencias y la configuración del proyecto, active el entorno virtual. En Windows, use: env\Scripts\activate
   En sistemas Unix o MacOS, use: source env/bin/activate
7. Instalación de Dependencias: Una vez activado el entorno virtual, instale las dependencias del proyecto ejecutando: pip install -r requirements.txt
8. Comprobación Dependencias: Ejecute el comando: python manage.py runserver
   ![image](https://github.com/criticalRobin/try_django_weasyprint/assets/133540422/b87c5d3c-65b3-4171-821d-86f6a0230478)
   Si obtiene un resultado como el de la imagen significa que los pasos anteriores fueron realizados con éxito.
9. Ejecutar Migraciones: Presione control+c para detener la ejecución de la app web, cuando se haya detenido ejecute el siguiente comando: python manage.py migrate
10. Crear Super Usuario: Finalmente ejecute el comando: python manage.py createsuperuser y complete el formulario de registro, con esto ya podrá acceder al admin view del proyecto de Django.
