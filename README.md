<h1 align="center">Laboratorio de Electrónica</h1>
<h2 align="center">Universidad de Pamplona</h2>

Pasos Instalación:

1. Si no tienen Python en su pc instalarlo. => https://www.python.org/downloads/
2. Instalar el paquete virtualenv. => pip install virtualenv
3. Clonar el repositorio. => https://github.com/wilmarmorales/laboratorio_electronica descargar como zip.
4. Se descomprime el zip donde va quedar la aplicación.
5. Creamos el entorno virtual con. => python -m virtualenv env
6. Activamos el entorno virtual. => env\Scripts\activate
7. Se instalan todos los paquetes necesarios que están en requirements.txt. => pip install -r requirements.txt
8. Compilamos la base de datos. => python manage.py makemigrations equipo login materia prestamo
9. Posteriormente migramos la base de datos. => python manage.py migrate
10. Creamos un superusuario. => python manage.py createsuperuser

Pasos para iniciar el aplicativo:

1. Activamos el entorno virtual. => env\Scripts\activate
2. Iniciamos el servidor. => python manage.py runserver
3. En el navegador iniciamos. => http://localhost:8000
