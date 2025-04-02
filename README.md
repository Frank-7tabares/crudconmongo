Título del Proyecto
CRUD Flask con MySQL

Comenzando 🚀
Este proyecto es una aplicación básica de CRUD (Create, Read, Update, Delete) desarrollada con Flask y MySQL.el profesor juan pablo gimenez nos pidio hcaer el mismo proyecto pero cambiando mongodb por mysql.

Mira Deployment para conocer como desplegar el proyecto.

Pre-requisitos 📋
Python 3.7 o superior
MySQL instalado y en ejecución (local o remoto)
Pip (gestor de paquetes de Python)
Instalación
Clonar el repositorio:
```bash
git clone [url-del-repositorio]
cd [nombre-del-directorio].

Instalación 🔧
python -m venv venv
source venv/bin/activate # Linux/Mac
venv\Scripts\activate # Windows.
pip install -r requirements.txt.

si no sabes

Ejecutando las pruebas ⚙️
es importante realizar todas las pruebas que sean necesarias para que todo salga nien ala hora de exponer tu proyecto.

Analice las pruebas end-to-end 🔩
estas pruebas verifican que todo lo que tiene la aplicacion funcione correctamente y no salga ningun error.

Da un ejemplo
Y las pruebas de estilo de codificación ⌨️
Explica que verifican estas pruebas y por qué

Da un ejemplo
Despliegue 📦
Agrega notas adicionales sobre como hacer deploy

Construido con 🛠️
visual studio code heidi xammp

Dropwizard - El framework web usado
Maven - Manejador de dependencias
ROME - Usado para generar RSS
Contribuyendo 🖇️
Por favor lee el CONTRIBUTING.md para detalles de nuestro código de conducta, y el proceso para enviarnos pull requests.

Wiki 📖
Puedes encontrar mucho más de cómo utilizar este proyecto en nuestra Wiki

Versionado 📌
Usamos SemVer para el versionado. Para todas las versiones disponibles, mira los tags en este repositorio.

Autores ✒️
frank-deepseek

Estructura del proyecto.
/proyecto
├── app.py # Aplicación principal Flask
├── database.py # Configuración y conexión a MySQL
├── models.py # Modelos de la base de datos
├── routes.py # Rutas de la aplicación
├── templates/ # Plantillas HTML
│ ├── base.html # Plantilla base
│ ├── create.html # Formulario de creación
│ ├── edit.html # Formulario de edición
│ └── index.html # Lista de elementos
├── requirements.txt # Dependencias
└── .env # Variables de entorno
Uso
CREATE DATABASE flask_crud;
python app.py
http://localhost:5000.

Endpoints disponibles.
GET / - Listar todos los elementos

GET /create - Mostrar formulario de creación

POST /create - Crear nuevo elemento

GET /edit/ - Mostrar formulario de edición

POST /edit/ - Actualizar elemento existente

GET /delete/ - Eliminar elemento

Tecnologías utilizadas.
MySQL - Sistema de gestión de bases de datos relacional

Flask-MySQLdb - Conector MySQL para Flask.


Licencia 📄
Flask==2.0.1
Flask-MySQLdb==2.0.0
