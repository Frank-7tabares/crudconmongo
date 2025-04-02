CRUD Flask con MySQL
Este proyecto es una aplicación básica de CRUD (Create, Read, Update, Delete) desarrollada con Flask y MySQL.el profesor juan pablo gimenez nos pidio hcaer el mismo proyecto pero cambiando mongodb por mysql.

Requisitos previos
Python 3.7 o superior
MySQL instalado y en ejecución (local o remoto)
Pip (gestor de paquetes de Python)
Instalación
Clonar el repositorio:
```bash
git clone [url-del-repositorio]
cd [nombre-del-directorio].

2.Crear y activar un entorno virtual.
python -m venv venv
source venv/bin/activate # Linux/Mac
venv\Scripts\activate # Windows.

3.Instalar las dependencias.
pip install -r requirements.txt.

Configuración.
Renombrar el archivo .env.example a .env.
DB_HOST=localhost # Host de la base de datos
DB_USER=root # Usuario de MySQL
DB_PASSWORD=password # Contraseña de MySQL
DB_NAME=flask_crud # Nombre de la base de datos

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
Flask - Framework web Python

MySQL - Sistema de gestión de bases de datos relacional

Flask-MySQLdb - Conector MySQL para Flask.

Licencia.
Flask==2.0.1
Flask-MySQLdb==2.0.0
