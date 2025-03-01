import json
import os

class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["id"], data["nombre"], data["cantidad"], data["precio"])


class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        self.productos[producto.id] = producto

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
            print("Producto eliminado correctamente.")
        else:
            print("No se encontró el producto con ese ID.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        if id in self.productos:
            if cantidad is not None:
                self.productos[id].cantidad = cantidad
            if precio is not None:
                self.productos[id].precio = precio
            print("Producto actualizado correctamente.")
        else:
            print("No se encontró el producto con ese ID.")

    def buscar_producto(self, nombre):
        resultados = [p for p in self.productos.values() if nombre.lower() in p.nombre.lower()]
        if resultados:
            for producto in resultados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_productos(self):
        if self.productos:
            for producto in self.productos.values():
                print(producto)
        else:
            print("No hay productos en el inventario.")

    def guardar_inventario(self, archivo="inventario.json"):
        datos = {id: p.to_dict() for id, p in self.productos.items()}
        with open(archivo, "w") as file:
            json.dump(datos, file, indent=4)
        print("Inventario guardado correctamente.")

    def cargar_inventario(self, archivo="inventario.json"):
        if os.path.exists(archivo):
            with open(archivo, "r") as file:
                datos = json.load(file)
                self.productos = {id: Producto.from_dict(data) for id, data in datos.items()}
            print("Inventario cargado correctamente.")
        else:
            print("No se encontró el archivo de inventario.")


def main():
    inventario = Inventario()

    while True:
        print("\nMenú de Inventario:")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar todos los productos")
        print("6. Guardar inventario")
        print("7. Cargar inventario")
        print("8. Salir")

        opcion = input("Ingrese su opción: ")

        if opcion == "1":
            id = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.agregar_producto(producto)
            print("Producto agregado correctamente.")

        elif opcion == "2":
            id = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id)

        elif opcion == "3":
            id = input("Ingrese el ID del producto a actualizar: ")
            cantidad = input("Ingrese la nueva cantidad (dejar vacío para no cambiar): ")
            precio = input("Ingrese el nuevo precio (dejar vacío para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id, cantidad, precio)

        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            inventario.guardar_inventario()

        elif opcion == "7":
            inventario.cargar_inventario()

        elif opcion == "8":
            print("Saliendo del programa.")
            break

        else:
            print("Opción inválida. Por favor, elija una opción del menú.")

if __name__ == "__main__":
    main()
