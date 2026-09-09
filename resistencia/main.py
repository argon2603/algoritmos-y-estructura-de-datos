import random

class Resistencia:
    def __init__(self):
        self.colores = [
            "Negro",    # 0
            "Marrón",   # 1
            "Rojo",     # 2
            "Naranja",  # 3
            "Amarillo", # 4
            "Verde",    # 5
            "Azul",     # 6
            "Violeta",  # 7
            "Gris",     # 8
            "Blanco"    # 9
        ]

    def determinar_colores(self, valor):
        str_val = str(valor)
        banda1 = self.colores[int(str_val[0])]
        banda2 = self.colores[int(str_val[1])]
        banda3 = self.colores[len(str_val) - 2]
        return [banda1, banda2, banda3]

    def calcular_serie(self, n):
        resistencias = []
        for _ in range(n):
            resistencias.append(random.randint(10, 1000000000))

        rts = 0
        for r in resistencias:
            rts += r

        return resistencias, rts

    def calcular_paralelo(self, n):
        resistencias = []
        for _ in range(n):
            resistencias.append(random.randint(10, 1000000000))

        rtp = 0
        for r in resistencias:
            rtp += 1 / r

        return resistencias, rtp


if __name__ == "__main__":
    resistencia = Resistencia()

    while True:
        print("\n1. Determinar colores")
        print("2. Resistencias en serie")
        print("3. Resistencias en paralelo")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            valor = input("Ingresa el valor de la resistencia (ej. 160, 5800): ")
            bandas = resistencia.determinar_colores(valor)
            print(f"Salida: {bandas[0]}, {bandas[1]}, {bandas[2]}")

        elif opcion == "2":
            n = int(input("¿Cuántas resistencias?: "))
            resistencias, rts = resistencia.calcular_serie(n)
            print("Resistencias:", resistencias)
            print("Rts =", rts)

        elif opcion == "3":
            n = int(input("¿Cuántas resistencias?: "))
            resistencias, rtp = resistencia.calcular_paralelo(n)
            print("Resistencias:", resistencias)
            print("Rtp =", rtp)

        elif opcion == "4":
            print("Fin del programa")
            break
        else:
            print("Opción inválida")