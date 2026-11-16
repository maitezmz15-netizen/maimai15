from flask import Flask, send_file
from index import crear_mapa
import os

app = Flask(__name__)

@app.route("/")
def inicio():
    crear_mapa()

    ruta_mapa = os.path.join(
        os.path.dirname(__file__),
        "templates",
        "mapa.html"
    )

    return send_file(ruta_mapa)

if __name__ == "__main__":
    app.run(debug=True)