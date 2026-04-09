from productos import ver_productos, productos
from pedidos import agregar_producto, ver_pedido, pedido_actual
from historial import guardar_compra, ver_historial

def menu():
    while True:
        print("""
--- TIENDA ---
1. Ver productos
2. Agregar producto al pedido
3. Ver mi pedido
4. Finalizar compra
5. Ver historial
6. Salir
""")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ver_productos()

        elif opcion == "2":
            id_producto = int(input("Ingrese ID del producto: "))
            cantidad = int(input("Cantidad: "))
            agregar_producto(productos, id_producto, cantidad)

        elif opcion == "3":
            ver_pedido()

        elif opcion == "4":
            total = ver_pedido()
            guardar_compra(pedido_actual, total)
            pedido_actual.clear()
            print("Compra guardada")

        elif opcion == "5":
            ver_historial()

        elif opcion == "6":
            print("Gracias por usar la tienda")
            break

        else:
            print("Opción inválida")


if __name__ == "__main__":
    menu()