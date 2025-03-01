# Semana-11.-Tarea-Fundamentos-de-colecciones
Sistema Avanzado de Gestión de Inventario

Explico.

Clase Producto. Define un producto con atributos id, nombre, cantidad, y precio. Incluye métodos para convertir el objeto a un diccionario (to_dict) y para crear un objeto desde un diccionario (from_dict).

Clase Inventario. Utiliza un diccionario para almacenar los productos donde cada clave es el ID del producto. Ofrece métodos para agregar, eliminar, actualizar productos, buscar por nombre, mostrar todos los productos, guardar el inventario en un archivo JSON y cargarlo.

Interfaz de Usuario. Un menú interactivo permite al usuario realizar operaciones sobre el inventario.

Almacenamiento en Archivos. El inventario se almacena en un archivo JSON, lo que permite persistencia entre sesiones del programa.

Colecciones. Se utilizan diccionarios para un acceso rápido a los productos por su ID y listas para operaciones como la búsqueda de productos por nombre.
