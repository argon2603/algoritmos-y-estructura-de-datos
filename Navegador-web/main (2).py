import os

class NavegadorWeb:
    def __init__(self, capacidad_maxima=5):
        self.pagina_actual = "Ninguna (Inicio)"
        self.back_stack = []
        self.forward_stack = []
        self.capacidad_maxima = capacidad_maxima
        self.mensaje_notificacion = ""

    def mostrar_pila(self, pila):
        if not pila:
            print("  (Vacío)")
            return
        # Muestra desde el elemento superior (tope) hacia abajo
        for i, elem in enumerate(reversed(pila), 1):
            print(f"  [{len(pila) - i + 1}] {elem}")

    def visitar(self, url):
        if self.pagina_actual and self.pagina_actual != "Ninguna (Inicio)":
            # Verificar si la pila atrás alcanzó su límite de capacidad
            if len(self.back_stack) >= self.capacidad_maxima:
                self.mensaje_notificacion = f"[!] Advertencia: PILA LLENA. Límite de {self.capacidad_maxima} páginas alcanzado."
            else:
                self.back_stack.append(self.pagina_actual)
                self.mensaje_notificacion = f"[!] Visitando nueva página: {url}"
        else:
            self.mensaje_notificacion = f"[!] Visitando nueva página: {url}"

        self.pagina_actual = url
        # Al visitar una nueva página, la pila adelante se limpia por completo
        self.forward_stack.clear()

    def back(self):
        if not self.back_stack:
            self.mensaje_notificacion = "[ERROR 404] PILA VACÍA: No hay páginas en la pila atrás para retroceder."
            return

        self.forward_stack.append(self.pagina_actual)
        self.pagina_actual = self.back_stack.pop()
        self.mensaje_notificacion = f"[<-] Retrocediendo a: {self.pagina_actual}"

    def forward(self):
        if not self.forward_stack:
            self.mensaje_notificacion = "[ERROR 404] PILA VACÍA: No hay páginas en la pila adelante para avanzar."
            return

        if len(self.back_stack) >= self.capacidad_maxima:
            self.mensaje_notificacion = f"[!] Advertencia: PILA LLENA. La página no se guardó en la pila atrás."
        else:
            self.back_stack.append(self.pagina_actual)
            self.mensaje_notificacion = f"[->] Avanzando a: {self.pagina_actual}"

    def mostrar_estado(self):
        print("=" * 54)
        print("                  ESTADO DEL NAVEGADOR                  ")
        print("=" * 54)
        # 1. Muestra la pila adelante primero
        print(" PILA ADELANTE (Forward Stack):")
        self.mostrar_pila(self.forward_stack)
        print("-" * 54)
        # 2. Muestra la pila atrás después
        print(f" PILA ATRÁS (Back Stack) [{len(self.back_stack)}/{self.capacidad_maxima}]:")
        self.mostrar_pila(self.back_stack)
        print("-" * 54)
        # 3. Muestra la página actual al final
        print(f" PÁGINA ACTUAL: {self.pagina_actual}")
        print("=" * 54)
        
        # Muestra notificaciones o errores del último movimiento
        if self.mensaje_notificacion:
            print(f"\n{self.mensaje_notificacion}\n" + "-" * 54)


def limpiar_pantalla():
    # Ejecuta 'cls' en Windows o 'clear' en Linux/macOS
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    navegador = NavegadorWeb(capacidad_maxima=5)

    while True:
        limpiar_pantalla()
        navegador.mostrar_estado()
        
        print("\n Menú :")
        print("1. Visitar página (URL)")
        print("2. Retroceder (Back)")
        print("3. Avanzar (Forward)")
        print("4. Salir (Exit)")
        
        opcion = input("\nSelecciona una opción (1-4): ").strip()

        if opcion == "1":
            url = input("Ingresa la URL: ").strip()
            if url:
                navegador.visitar(url)
            else:
                navegador.mensaje_notificacion = "[ERROR] La URL no puede estar vacía."
        elif opcion == "2":
            navegador.back()
        elif opcion == "3":
            navegador.forward()
        elif opcion == "4":
            limpiar_pantalla()
            print("Cerrando el navegador...")
            break
        else:
            navegador.mensaje_notificacion = "[ERROR] Opción no válida. Intenta de nuevo."

if __name__ == "__main__":
    main()