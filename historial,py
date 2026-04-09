def guardar_compra(pedido, total):
    with open("data/historial.txt", "a") as f:
        f.write("Nueva compra:\n")
        for item in pedido:
            f.write(f"{item['nombre']} x{item['cantidad']} - ${item['precio']}\n")
        f.write(f"TOTAL: ${total}\n\n")


def ver_historial():
    print("\n--- HISTORIAL DE COMPRAS ---")
    try:
        with open("data/historial.txt", "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("No hay compras registradas")