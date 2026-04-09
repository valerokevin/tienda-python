productos = [
    {"id": 1, "nombre": "Manzana", "precio": 1000},
    {"id": 2, "nombre": "Pan", "precio": 2000},
    {"id": 3, "nombre": "Leche", "precio": 3000},
]

def ver_productos():
    print("\n--- LISTA DE PRODUCTOS ---")
    for p in productos:
        print(f"{p['id']}. {p['nombre']} - ${p['precio']}")