# Ebanisteria_Leon_Back

_Ebanisteria leon es un aplicativo web, en el cual se exiben todo tipo de muebles, este está pensado para las personas que tienen la dificultad para ver los productos de la Ebanisteria Leon._

## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._
Mira **Deployment** para conocer como desplegar el proyecto.

### Pre-requisitos 📋

_Que cosas necesitas para instalar el software y como instalarlas_

```
Python, Django rest framework
```

### Instalación 🔧

_Paso a paso para tener el entorno de desarrollo del proyecto._

_Instalacion de Python_

```
Es necesario visitar el sitio web de python, accediento a este link: https://www.python.org/downloads/
Despues se selecciona el boton de download, al finalizar la descarga se abre el ejecutable
y se selecciona la casilla que dice PATH
Comienza la instalacion, con siguiente, siguiente y finalizar.
```

_Instalacion del entorno virtual_

```
Para crear el entorno virtaul es necesario instalar Python. Abrimos una consola y ponemos el comando:
pip install virtualenv, luego validamos si esta instalado con el comando virtualenv --version
por ultimo accedemos a una carpeta y habrimos la consola y ejecutamos el comando virtualenv 'nombreCarpeta'
accedemos a la carpeta e iniciamos el entorno virtual

.\test\Scripts\activate

Finalmente desactivamos el entorno virtual

deactivate.
```

_Instalar Django Rest Framework_

```
Para inatalar Django es necesario acceder a la carpeta raíz del proyecto, abrir la consola y
ejecutar el siguiente comando pip install -r requirements.txt o poner pip install -r r + Tab
para autocompletqar el nombre del archivo, en este archivo se encuentran los requerimientos para
tener el proyecto funcional en local
```

_Base de datos local en SQLite 3_
```
Django ya nos provee una base de datos local la cual es SQLite, esta es creada al momento de ejecutar
el proyecto por primera vez con el comando python manage.py runserver o haciendo sus respectivas migraciones,
colocando los siguientes comandos: python manage.py makemigrations users, luego se hace el mismo pero se cambia
el users por products y por ultimo se cambia por expense_manager, por ultimo ejecutamos el comando
python manage.py migrate, con este tenemos la base de datos lista para ser utilizada
```

## Construido con 🛠️

_herramientas para _

* [Django](http://www.dropwizard.io/1.0.2/docs/) - El framework web usado
* [Pip](https://maven.apache.org/) - Manejador de dependencias

## Autores ✒️

_Colaboradores del proyecto_

* **Gojan Holguin Rincon** - *Trabajo del BackEnd* - [Gohan-117holguin](https://github.com/Gohan-117holguin)
* **Marlon Andres Campo** - Trabajo del FrontEnd* - [ItzMarlon2](https://github.com/ItzMarlon2)
* **Alexander Correa Diaz** - *Documentación* - [dicoaa](https://github.com/dicoaa)
* **Micheal Valencia Tapiero** - *Tester* - [valencia07](https://github.com/valencia07)

## Expresiones de Gratitud 🎁

* Comenta a otros sobre este proyecto 📢
* Invita una cerveza 🍺 o un café ☕ a alguien del equipo. 
