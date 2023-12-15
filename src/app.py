from flask import Flask
from flask import render_template
from flaskext.mysql import mySQL

app = Flask(__name__)
mysql = mySQL()

if __name__=='__main__':
    app.run(debug=True)

""" comentado
@app.route("/hola")
def hello():
    return "<p>Hola, Mundo! App</p>"

@app.route("/chau")
def bye():
    return "<p>chau, Mundo!</p>"

@app.route("/contacto")
def contactoHandling():
    return "contacto guardado"
    
"""