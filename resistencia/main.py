import random

colores = [
    "Negro",
    "Marrón",
    "Rojo",
    "Naranja",
    "Amarillo",
    "Verde",
    "Azul",
    "Violeta",
    "Gris",
    "Blanco"
]

while True:
    print("\n1. Determinar colores")
    print("2. Resistencias en serie")
    print("3. Resistencias en paralelo")
    print("4. Salir")
    
    opcion = input("Elige una opción: ")

    if opcion == "1":
        valor = input("Ingresa el valor de la resistencia (ej. 160, 5800): ")
        
        banda1 = colores[int(valor[0])]
        banda2 = colores[int(valor[1])]
        banda3 = colores[len(valor) - 2]
        
        print(f"Salida: {banda1}, {banda2}, {banda3}")

    elif opcion == "2":
        n = int(input("¿Cuántas resistencias?: "))
        resistencias = []
        
        for i in range(n):
            resistencias.append(random.randint(10, 1000000000))
            
        print("Resistencias:", resistencias)
        
        rts = sum(resistencias)
        print("Rts =", rts)

    elif opcion == "3":
        n = int(input("¿Cuántas resistencias?: "))
        resistencias = []
        
        for i in range(n):
            resistencias.append(random.randint(10, 1000000000))
            
        print("Resistencias:", resistencias)
        
        rtp = 0
        for r in resistencias:
            rtp += 1 / r
            
        print("Rtp =", rtp)

    elif opcion == "4":
        print("Fin del programa")
        break
    else:
        print("Opción inválida")