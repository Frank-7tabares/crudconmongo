Título del Proyecto
CRUD Flask con MongoDB

Comenzando 🚀
Este proyecto es una aplicación básica de CRUD (Create, Read, Update, Delete) desarrollada con Flask y MongoDB utilizando PyMongo como conector. el profesor juan pablo jimenez nos pidio desarrolar un crub utilizando mongodb luego subirla a git con sus respectivos commits y su diagrama sobre su funcionamiento.

Mira Deployment para conocer como desplegar el proyecto.

Pre-requisitos 📋
Python 3.7 o superior
MongoDB instalado y en ejecución (local o remoto)
Pip (gestor de paquetes de Python)
Instalación

Da un ejemplo
Instalación 🔧
Clonar el repositorio:
```bash
git clone [url-del-repositorio]
cd [nombre-del-directorio]
Crear y activar un entorno virtual.
python -m venv venv
source venv/bin/activate # Linux/Mac
venv\Scripts\activate # Windows.

Dí cómo será ese paso

Da un ejemplo
Y repite

hasta finalizar
Finaliza con un ejemplo de cómo obtener datos del sistema o como usarlos para una pequeña demo

Ejecutando las pruebas ⚙️
Explica como ejecutar las pruebas automatizadas para este sistema.Renombrar el archivo .env.example a .env.
.MONGO_URI=mongodb://localhost:27017 # URL de conexión a MongoDB
DATABASE_NAME=flask_crud # Nombre de la base de datos.

Analice las pruebas end-to-end 🔩
analisa muy bien tu proyecto antes de ejecutarlo si te sale error intenta resolverlo por si solo si no puedes ayudate con las diferentes ia que existen.

Da un ejemplo
estas pruebas verifican que tu proyecto funciona correctamentre y no vas atener inconveniente a la hora de exponerlo ⌨️



Despliegue 📦
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

Construido con 🛠️
visual studio code mongodb y deepseek

Tecnologías utilizadas.
Flask - Framework web Python

PyMongo - Conector oficial de Python para MongoDB.


Versionado 📌
Usamos SemVer para el versionado. Para todas las versiones disponibles, mira los tags en este repositorio.

Autores ✒️
frank y deepseek.


Licencia 📄
Flask==2.0.1
pymongo==4.0.1
