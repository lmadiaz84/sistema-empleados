from flask import Flask

app = Flask(__name__)

@app.route("/hola")
def hello():
    return "<p>Hola, Mundo! App</p>"

@app.route("/chau")
def bye():
    return "<p>chau, Mundo!</p>"

@app.route("/contacto")
def contactoHandling():
    return "contacto guardado"