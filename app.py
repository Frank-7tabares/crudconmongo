from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId  # Importa ObjectId para manejar los IDs de MongoDB

app = Flask(__name__)

# Conexión a MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["biblioteca"]

# Ruta para la página principal
@app.route("/")
def index():
    usuarios = db.usuarios.find()
    return render_template("index.html", usuarios=usuarios)

# Ruta para agregar un usuario
@app.route("/agregar", methods=["GET", "POST"])
def agregar():
    if request.method == "POST":
        nombre = request.form["nombre"]
        email = request.form["email"]
        telefono = request.form["telefono"]
        db.usuarios.insert_one({"nombre": nombre, "email": email, "telefono": telefono})
        return redirect(url_for("index"))
    return render_template("agregar.html")

# Ruta para editar un usuario
@app.route("/editar/<id>", methods=["GET", "POST"])
def editar(id):
    try:
        usuario = db.usuarios.find_one({"_id": ObjectId(id)})  # Usa ObjectId para buscar el usuario
        if request.method == "POST":
            nombre = request.form["nombre"]
            email = request.form["email"]
            telefono = request.form["telefono"]
            db.usuarios.update_one({"_id": ObjectId(id)}, {"$set": {"nombre": nombre, "email": email, "telefono": telefono}})
            return redirect(url_for("index"))
        return render_template("editar.html", usuario=usuario)
    except Exception as e:
        return f"Error: {str(e)}", 400

# Ruta para eliminar un usuario
@app.route("/eliminar/<id>", methods=["POST"])
def eliminar(id):
    try:
        db.usuarios.delete_one({"_id": ObjectId(id)})  # Usa ObjectId para eliminar el usuario
        return redirect(url_for("index"))
    except Exception as e:
        return f"Error: {str(e)}", 400

if __name__ == "__main__":
    app.run(debug=True)