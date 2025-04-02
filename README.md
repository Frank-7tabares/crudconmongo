CRUD Flask con MongoDB
Este proyecto es una aplicación básica de CRUD (Create, Read, Update, Delete) desarrollada con Flask y MongoDB utilizando PyMongo como conector. el profesor juan pablo jimenez nos pidio desarrolar un crub utilizando mongodb luego subirla a git con sus respectivos commits y su diagrama sobre su funcionamiento.

Requisitos previos
Python 3.7 o superior
MongoDB instalado y en ejecución (local o remoto)
Pip (gestor de paquetes de Python)
Instalación
Clonar el repositorio:
```bash
git clone [url-del-repositorio]
cd [nombre-del-directorio]
Crear y activar un entorno virtual.
python -m venv venv
source venv/bin/activate # Linux/Mac
venv\Scripts\activate # Windows.
3.Instalar las dependencias.
pip install -r requirements.txt.
4.Renombrar el archivo .env.example a .env.
5.MONGO_URI=mongodb://localhost:27017 # URL de conexión a MongoDB
DATABASE_NAME=flask_crud # Nombre de la base de datos.
Estructura del proyecto.
/proyecto
├── app.py # Aplicación principal Flask
├── models.py # Modelos y conexión a MongoDB
├── routes.py # Rutas de la aplicación
├── templates/ # Plantillas HTML
│ ├── base.html # Plantilla base
│ ├── create.html # Formulario de creación
│ ├── edit.html # Formulario de edición
│ └── index.html # Lista de elementos
├── requirements.txt # Dependencias
└── .env # Variables de entorno.

Uso.
python app.py.
http://localhost:5000.

Endpoints disponibles.
GET / - Listar todos los elementos

GET /create - Mostrar formulario de creación

POST /create - Crear nuevo elemento.

GET /edit/ - Mostrar formulario de edición

POST /edit/ - Actualizar elemento existente

GET /delete/ - Eliminar elemento.

Tecnologías utilizadas.
Flask - Framework web Python

PyMongo - Conector oficial de Python para MongoDB.

Licencia.
Flask==2.0.1
pymongo==4.0.1
