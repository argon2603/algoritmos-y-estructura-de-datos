# Fase 4. Codificación - Sistema de Carrito de Compras
# Estructuras de Datos y Algoritmos - Universidad Anáhua
import os

# CLASES DEL SISTEMA

class Producto:
    """Clase que modela los datos de un artículo del catálogo."""
    def __init__(self, id: int, nombre: str, categoria: str, precio: float):
        # Atributos definidos en el diseño UML
        self.id = id
        self.nombre = nombre
        self.categoria = categoria
        self.precio = float(precio)

    # Métodos Getter
    def getID(self):
        return self.id

    def getNombre(self):
        return self.nombre

    def getCategoria(self):
        return self.categoria

    def getPrecio(self):
        return self.precio

    def __str__(self):
        return f"{self.id} | {self.nombre} | {self.categoria} | ${self.precio:.2f}"


class ElementoCarrito:
    """Clase que representa un ítem dentro del carrito (asocia un producto con su cantidad)."""
    def __init__(self, producto: Producto, cantidad: int):
        self.producto = producto
        self.cantidad = int(cantidad)

    def getProducto(self):
        return self.producto

    def getCantidad(self):
        return self.cantidad

    def setCantidad(self, nuevaCantidad: int):
        self.cantidad = nuevaCantidad

    def calcularSubtotal(self):
        # Fórmula codificada para el subtotal
        return self.producto.getPrecio() * self.cantidad
    
    def __str__(self):
        return f"{self.producto.getID()} | {self.producto.getNombre()} | ${self.producto.getPrecio():.2f} | {self.cantidad} | ${self.calcularSubtotal():.2f}"


class CarritoDeCompras:
    """Clase principal que administra el catálogo y las operaciones del carrito."""
    def __init__(self):
        # Uso obligatorio de listas como estructura de datos
        self.catalogo = []
        self.itemsCarrito = []
        self.cargarCatalogoInicial()

    def cargarCatalogoInicial(self):
        """Carga los productos predefinidos en la lista del catálogo en memoria."""
        self.catalogo.append(Producto(1, "Teclado", "Accesorios", 450.0))
        self.catalogo.append(Producto(2, "Mouse", "Accesorios", 250.0))
        self.catalogo.append(Producto(3, "Monitor", "Electrónica", 3200.0))
        self.catalogo.append(Producto(4, "Audifonos", "Audio", 800.0))
        self.catalogo.append(Producto(5, "Memoria USB", "Almacenamiento", 180.0))

    def mostrarCatalogo(self):
        """R1: Muestra en pantalla el catálogo completo."""
        print("\n--- CATÁLOGO DE PRODUCTOS ---")
        print("ID | Producto | Categoría | Precio")
        print("-" * 40)
        for prod in self.catalogo:
            print(prod)
        print("-" * 40)

    def buscarProducto(self, criterio: str):
        """R2: Busca un producto en el catálogo por ID o por nombre (búsqueda secuencial)."""
        criterioBusqueda = str(criterio).lower()
        for prod in self.catalogo:
            if str(prod.getID()) == criterioBusqueda or prod.getNombre().lower() == criterioBusqueda:
                return prod
        return None

    def agregarProducto(self, idONombre: str, cantidad: int):
        """R3: Agrega un producto al carrito o incrementa la cantidad si ya existe."""
        if cantidad <= 0:
            print("ERROR. La cantidad debe ser mayor a 0.")
            return False

        producto = self.buscarProducto(idONombre)
        if not producto:
            print("ERROR. Producto no encontrado en el catálogo.")
            return False

        # Verifica si ya existe en el carrito
        for item in self.itemsCarrito:
            if item.getProducto().getID() == producto.getID():
                item.setCantidad(item.getCantidad() + cantidad)
                print(f"\n¡Producto actualizado! {producto.getNombre()} | Cantidad total: {item.getCantidad()}")
                return True
        
        # Si no existe, lo inserta en la lista
        nuevoItem = ElementoCarrito(producto, cantidad)
        self.itemsCarrito.append(nuevoItem)
        print(f"\nProducto: {producto.getNombre()}")
        print(f"Precio unitario: ${producto.getPrecio():.2f}")
        print("¡Producto agregado al carrito!")
        return True

    def verCarrito(self):
        """R4: Lista los artículos del carrito con sus subtotales y el total."""
        print("\n--- CARRITO DE COMPRAS ---")
        if not self.itemsCarrito:
            print("(El carrito está vacío)")
            return

        print(f"{'ID':<4} | {'Producto':<15} | {'Precio':<8} | {'Cant.':<5} | {'Subtotal':<10}")
        print("-" * 55)
        
        for item in self.itemsCarrito:
            prod = item.getProducto()
            print(f"{prod.getID():<4} | {prod.getNombre():<15} | ${prod.getPrecio():<7.2f} | {item.getCantidad():<5} | ${item.calcularSubtotal():<9.2f}")
        
        print("-" * 55)
        print(f"TOTAL: ${self.calcularTotal():.2f}")

    def modificarCantidad(self, idProducto: int, nuevaCantidad: int):
        """R5: Actualiza la cantidad de un producto ya agregado."""
        if nuevaCantidad <= 0:
            print("ERROR. La cantidad debe ser mayor a 0.")
            return False

        for item in self.itemsCarrito:
            if item.getProducto().getID() == idProducto:
                print(f"Producto: {item.getProducto().getNombre()}")
                print(f"Cantidad actual: {item.getCantidad()}")
                item.setCantidad(nuevaCantidad)
                print("¡Cantidad actualizada!")
                return True
        
        print("ERROR. El producto no está en el carrito.")
        return False

    def eliminarProducto(self, idProducto: int):
        """R6: Elimina un producto específico del carrito pidiendo confirmación."""
        for i in range(len(self.itemsCarrito)):
            if self.itemsCarrito[i].getProducto().getID() == idProducto:
                print(f"Producto: {self.itemsCarrito[i].getProducto().getNombre()}")
                confirmacion = input("¿Está seguro que desea eliminar este producto? (s/n): ").strip().lower()
                if confirmacion == 's':
                    self.itemsCarrito.pop(i)
                    print("¡Producto eliminado del carrito!")
                    return True
                else:
                    print("Operación cancelada.")
                    return False
        
        print("ERROR. El producto no está en el carrito.")
        return False

    def vaciarCarrito(self):
        """R7: Limpia por completo la lista del carrito con confirmación."""
        if not self.itemsCarrito:
            print("El carrito ya está vacío.")
            return

        self.verCarrito()
        confirmacion = input("\n¿Está seguro que desea vaciar el carrito? (s/n): ").strip().lower()
        if confirmacion == 's':
            self.itemsCarrito.clear()
            print("¡Carrito vaciado!")
        else:
            print("Operación cancelada.")

    def calcularTotal(self):
        """Calcula la suma acumulada de todos los subtotales."""
        totalPagar = 0.0
        for item in self.itemsCarrito:
            totalPagar += item.calcularSubtotal()
        return totalPagar

    def calcularTotalArticulos(self):
        """Calcula la suma física de unidades agregadas al carrito."""
        totalArticulos = 0
        for item in self.itemsCarrito:
            totalArticulos += item.getCantidad()
        return totalArticulos

    def finalizarCompra(self):
        """R8: Procesa la compra y muestra el resumen de transacción final."""
        if not self.itemsCarrito:
            print("\nNo hay artículos en el carrito para comprar.")
            return

        print("\n--- RESUMEN DE COMPRA ---")
        print(f"{'ID':<4} | {'Producto':<15} | {'Cant.':<5} | {'Subtotal':<10}")
        print("-" * 45)
        for item in self.itemsCarrito:
            prod = item.getProducto()
            print(f"{prod.getID():<4} | {prod.getNombre():<15} | {item.getCantidad():<5} | ${item.calcularSubtotal():<9.2f}")
        
        print("-" * 45)
        print(f"Productos distintos: {len(self.itemsCarrito)}")
        print(f"Total de artículos: {self.calcularTotalArticulos()}")
        print(f"Total a pagar: ${self.calcularTotal():.2f}")
        print("\nGracias por su compra.")


# --- FUNCIONES AUXILIARES Y CONTROL PRINCIPAL ---

def limpiarPantalla():
    """Limpia la consola según el sistema operativo."""
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    tienda = CarritoDeCompras()

    while True:
        limpiarPantalla()
        print("\n--- MENÚ PRINCIPAL - CARRITO DE COMPRAS ---")
        print("1. Mostrar catálogo")
        print("2. Buscar producto")
        print("3. Agregar producto al carrito")
        print("4. Ver carrito")
        print("5. Modificar cantidad")
        print("6. Eliminar producto")
        print("7. Vaciar carrito")
        print("8. Finalizar compra")
        print("9. Salir")
        
        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == "1":
            limpiarPantalla()
            tienda.mostrarCatalogo()
            input("\nPresione ENTER para volver al menú...")

        elif opcion == "2":
            limpiarPantalla()
            tienda.mostrarCatalogo()
            busqueda = input("\nBuscar producto (Ingrese ID o Nombre): ").strip()
            resultado = tienda.buscarProducto(busqueda)
            if resultado:
                print("\n--- Resultado de la búsqueda ---")
                print(f"ID: {resultado.getID()}")
                print(f"Producto: {resultado.getNombre()}")
                print(f"Categoría: {resultado.getCategoria()}")
                print(f"Precio: ${resultado.getPrecio():.2f}")
            else:
                print("\nERROR. Producto no encontrado.")
            input("\nPresione ENTER para continuar...")

        elif opcion == "3":
            limpiarPantalla()
            tienda.mostrarCatalogo()
            idONombre = input("\nID o Nombre del producto a agregar: ").strip()
            try:
                cantidad = int(input("Cantidad: "))
                tienda.agregarProducto(idONombre, cantidad)
            except ValueError:
                # Manejo de errores básicos y validación
                print("ERROR. Debe ingresar un valor numérico entero para la cantidad.")
            input("\nPresione ENTER para continuar...")

        elif opcion == "4":
            limpiarPantalla()
            tienda.verCarrito()
            input("\nPresione ENTER para volver al menú...")

        elif opcion == "5":
            limpiarPantalla()
            tienda.verCarrito()
            try:
                idProducto = int(input("\nID del producto a modificar: "))
                nuevaCantidad = int(input("Nueva cantidad: "))
                tienda.modificarCantidad(idProducto, nuevaCantidad)
            except ValueError:
                print("ERROR. Los valores ingresados deben ser numéricos enteros.")
            input("\nPresione ENTER para continuar...")

        elif opcion == "6":
            limpiarPantalla()
            tienda.verCarrito()
            try:
                idProducto = int(input("\nID del producto a eliminar: "))
                tienda.eliminarProducto(idProducto)
            except ValueError:
                print("ERROR. El ID debe ser un valor numérico entero.")
            input("\nPresione ENTER para continuar...")

        elif opcion == "7":
            limpiarPantalla()
            tienda.vaciarCarrito()
            input("\nPresione ENTER para volver al menú...")

        elif opcion == "8":
            limpiarPantalla()
            tienda.finalizarCompra()
            if tienda.itemsCarrito:
                tienda.itemsCarrito.clear()
            input("\nPresione ENTER para volver al menú...")

        elif opcion == "9":
            limpiarPantalla()
            print("Gracias por usar el programa. ¡Hasta pronto!\nPrograma finalizado.")
            break

        else:
            print("\nERROR. Opción no válida. Intente de nuevo.")
            input("Presione ENTER para continuar...")

if __name__ == "__main__":
    main()