import folium
import sqlite3
import os

def crear_mapa():
    
    ruta_db = os.path.join(os.path.dirname(__file__), "lugares.db")
    conexion = sqlite3.connect(ruta_db)
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM lugares")
    lugares = cursor.fetchall()
    print("Lugares encontrados en SQLite:", len(lugares))
    print(lugares)

    conexion.close()

    # 1. Crear el mapa centrado en la escuela
    mi_mapa = folium.Map(
        location=[-33.701414, -65.498764],
        zoom_start=15
    )

    # 2. Lista de instituciones
    instituciones = [
        {
            "nombre": "Escuela Pública Bilingüe Digital Mahatma Gandhi",
            "descripcion": """
                <b>Nivel Inicial, Primario y Secundario</b><br>
                Barrio La Ribera<br>
                <img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSrnxgYIaqnQwi-bKwTIhtmOEGDyixcIkdCxEpZN1j0UQ&s=10' width='200px' style='border-radius: 5px; margin-top: 5px;'>
            """,
            "coords": [-33.701414, -65.498764],
            "icono": "graduation-cap",
            "color": "blue"
        },
        {
            "nombre": "Hospital Dr Braulio Moyano",
            "descripcion": "Hospital - Barrio La Ribera",
            "coords": [-33.6949343717328, -65.50563353800183],
            "icono": "hospital",
             "color": "red"
        }
    ]

    # 3. Agregar marcadores al mapa
    for inst in instituciones:

        folium.Marker(
            location=inst["coords"],
            popup=f"<b>{inst['nombre']}</b><br>{inst['descripcion']}",
            tooltip=inst["nombre"],
            icon=folium.Icon(
                color=inst["color"],
                icon=inst["icono"],
                prefix="fa"
            )
        ).add_to(mi_mapa)

            # Agregar los lugares obtenidos de SQLite
    for lugar in lugares:

        folium.Marker(
            location=[lugar[5], lugar[6]],
            popup=f"<b>{lugar[1]}</b><br>{lugar[2]}<br>{lugar[3]}",
            tooltip=lugar[1],
            icon=folium.Icon(
                color="purple",
                icon="info-sign",
                prefix="glyphicon"
            )
        ).add_to(mi_mapa)

    # 4. Guardar el mapa
    ruta_mapa = os.path.join(
    os.path.dirname(__file__),
    "templates",
    "mapa.html"
)
    os.makedirs(os.path.dirname(ruta_mapa), exist_ok=True)
    mi_mapa.save(ruta_mapa)

    print("Mapa de Villa Mercedes generado correctamente.")

if __name__ == "__main__":
    crear_mapa()
