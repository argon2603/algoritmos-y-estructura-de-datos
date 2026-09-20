
import random

cola = []
capacidad_maxima = 6
pcs = ["PC1", "PC2", "PC3", "PC4", "PC5"]

opcion = ""


while opcion != "3":
    
    print("\n--------------------------------")
    print("Estado actual de la cola:", cola)
    print("Espacio ocupado:", len(cola), "de", capacidad_maxima)
    print("--------------------------------")
    
    
    print("1. Agregar trabajo")
    print("2. Imprimir documento")
    print("3. Salir")
    
    opcion = input("Selecciona una opción: ")

    
    if opcion == "1":
        if len(cola) >= capacidad_maxima:
            print("\n La cola de impresión está LLENA")
        else:
            pc_aleatoria = random.choice(pcs)
            cola.append(pc_aleatoria)  
            print("\nSe agregó:", pc_aleatoria)

   
    elif opcion == "2":
        if len(cola) == 0:
            print("\n La cola de impresión está VACÍA")
        else:
            atendido = cola.pop(0)  
            print("\n🖨️ Impresión", atendido)

    
    elif opcion == "3":
        print("\n¡Hasta luego!")

    else:
        print("\nOpción no válida, intenta de nuevo.")