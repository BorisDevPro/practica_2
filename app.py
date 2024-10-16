from flask import Flask,request, render_template, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/index.html")
def inicio():
    return render_template("index.html")

@app.route("/contacto.html")
def contactos():
    return render_template("contacto.html")

@app.route("/noticias.html")
def noticias():
    return render_template("noticias.html")

@app.route("/quienes_somos.html")
def quienes_somos():
    return render_template("quienes_somos.html")

@app.route("/servicios.html")
def servicios():
    return render_template("servicios.html")


if __name__ == "__main__":
    app.run(debug=True)
