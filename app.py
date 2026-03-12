from flask import Flask, render_template, request, redirect
import sqlite3
import datetime

app = Flask(__name__)

def conectar():
    return sqlite3.connect("database.db")

@app.route("/")
def inicio():
    return render_template("registro.html")

@app.route("/registrar", methods=["POST"])
def registrar():

    nombre = request.form["nombre"]
    edad = request.form["edad"]
    telefono = request.form["telefono"]
    clase = request.form["clase"]

    fecha = datetime.date.today()

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO estudiantes(nombre,edad,telefono,clase,fecha)
    VALUES(?,?,?,?,?)
    """,(nombre,edad,telefono,clase,fecha))

    conn.commit()
    conn.close()

    return redirect("/dashboard")

@app.route("/dashboard")
def dashboard():

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM estudiantes WHERE fecha=date('now')")
    hoy = cursor.fetchone()[0]

    cursor.execute("SELECT nombre,clase FROM estudiantes WHERE fecha=date('now')")
    lista = cursor.fetchall()

    conn.close()

    return render_template("dashboard.html", hoy=hoy, lista=lista)

app.run(debug=True)