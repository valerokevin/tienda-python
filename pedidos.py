pedido_actual = []

def agregar_producto(productos, id_producto, cantidad):
    for p in productos:
        if p["id"] == id_producto:
            pedido_actual.append({
                "nombre": p["nombre"],
                "precio": p["precio"],
                "cantidad": cantidad
            })
            print("Producto agregado al pedido")
            return
    print("Producto no encontrado")


def ver_pedido():
    print("\n--- MI PEDIDO ---")
    total = 0
    for item in pedido_actual:
        subtotal = item["precio"] * item["cantidad"]
        total += subtotal
        print(f"{item['nombre']} x{item['cantidad']} = ${subtotal}")
    print(f"TOTAL: ${total}")
    return total