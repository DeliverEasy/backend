# DeliverEasy/backend

Seccion de backend del proyecto "DeliverEasy"

## Getting Started

### Prerquisitos

#### Paquetes

| Paquetes | Version |
|:---|:---:|
| Django | 2.1.3 |
| django-cors-headers | 2.4.0 |
| djangorestframework | 3.9.0 |
| djangorestframework-jwt | 1.11.0 |
| pkg-resources | 0.0.0 |
| PyJWT | 1.6.4 |
| pytz | - |

### Instalacion

#### Descarga de archivos de repositorio

Para descargar los archivos de este repositorio tendremos que ejecutar los siguientes comandos en terminal
'''
git init

git clone https://github.com/DeliverEasy/backend.git
'''

#### (Opcional) Creacion e utilizacion de virtual enviroment

Para crear un entorno virtual donde se instalaran los paquetes para el proyecto hay que ejecutar el siguiente comando en terminal
'''
python3 -m venv [directory]
'''

Y para activar el entorno virtual ejecutaremos 
'''
source [directory]/bin/activate
'''

#### Instalacion de paquetes

Los paquetes necesarios se pueden utilizar el siguiente comando de terminal
'''
pip install -r requirements.txt
'''
Tener en cuenta que hay que acceder primero a la carpeta root (.../core), donde esta localizado el archivo 'requirements.txt'

## Testeo

Para testear el funcionamiento de REST Framework utilizaremos el siguiente comando
'''
# Dentro de la carpeta root (core)

python3 manage.py runserver
'''

Luego entrar con un browser (Google Chrome, Internet Explorer, etc...) al url...
'''
http://localhost:8000/token-auth/
'''

## Built with
* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/)
* [Django REST Framework](http://www.django-rest-framework.org/)
* [Django REST Framework JWT](http://getblimp.github.io/django-rest-framework-jwt/)
* [Django CORS Headers](https://github.com/ottoyiu/django-cors-headers/)