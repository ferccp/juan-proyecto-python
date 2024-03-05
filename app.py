# importar la clase de Flask
from flask import Flask

# crear una instacia de Flask
# crear una varible app
# __name__ es una variable especial esta dice enq ue fichero estoy ejecutando Python esta tambien dice a donde va ir el hilo principal 
app = Flask(__name__)

# crear una route/endpoint
# crear un decorador. es una funcion que llama a otro funcion
@app.route("/")
def inicio(): #crear funcion
        return "Hola Mundo"

@app.route("/contactos")
def contactos():
        return "<h4> Hola, estoy en contactos </4>"

@app.route("/getJson", methods=["GET"])
def getJson():
        return {
                "nombre": "Juan Jose Roberto", "tipo": "estudiante"
                }

        

# AHORA DEBO EJECUTAR FLASK
# Debo reconcoer si estoy en programam principal

if __name__ == "__main__":
        app.run(debug=True)
