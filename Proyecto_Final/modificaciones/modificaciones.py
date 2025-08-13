from conexionBD import conexion, cursor
from funciones import borrarPantalla, esperarTecla

# Función para editar un producto existente
def editarProducto():
    borrarPantalla()
    try:
        id_producto = int(input("🆔 Ingresa el ID del producto a editar: "))
        nuevo_nombre = input("📦 Nuevo nombre del producto: ").strip()
        nuevo_precio = float(input("💵 Nuevo precio: "))
        nuevo_stock = int(input("📦 Nuevo stock: "))

        sql = "UPDATE productos SET nombre = %s, precio = %s, stock = %s WHERE id = %s"
        val = (nuevo_nombre, nuevo_precio, nuevo_stock, id_producto)
        cursor.execute(sql, val)
        conexion.commit()

        print("✅ Producto actualizado correctamente.")
    except Exception as e:
        print(f"❌ Error al actualizar el producto: {e}")


# Función para eliminar un producto por su ID
def eliminarProducto():
    borrarPantalla()
    try:
        id_producto = input("🆔 Ingresa el ID del producto a eliminar: ").strip()

        # Validar que sea un número
        if not id_producto.isdigit():
            print("⚠️ El ID debe ser un número válido.")
            return

        confirmar = input(f"⚠️ ¿Seguro que quieres eliminar el producto con ID {id_producto}? (s/n): ").strip().lower()
        if confirmar != "s":
            print("❌ Eliminación cancelada.")
            return

        sql = "DELETE FROM productos WHERE id = %s"
        val = (id_producto,)
        cursor.execute(sql, val)
        conexion.commit()

        if cursor.rowcount > 0:
            print("✅ Producto eliminado correctamente.")
        else:
            print("⚠️ No se encontró un producto con ese ID.")

    except Exception as e:
        print(f"❌ Error al eliminar el producto: {e}")
