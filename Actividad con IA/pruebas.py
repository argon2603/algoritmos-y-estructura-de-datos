"""
Pruebas del ABB de palabras. Ejecutar con:  python pruebas.py
Cada caso compara el resultado obtenido contra el esperado.
"""

from arbol_palabras import construir_arbol

resultados = []


def verificar(nombre, obtenido, esperado):
    ok = obtenido == esperado
    resultados.append(ok)
    estado = "OK   " if ok else "FALLA"
    print(f"[{estado}] {nombre}")
    if not ok:
        print(f"         esperado: {esperado}")
        print(f"         obtenido: {obtenido}")


# Caso 1: inserción y recorridos
a = construir_arbol("gato perro casa")
verificar("1. inorden", a.inorden(), ["casa", "gato", "perro"])
verificar("1. preorden", a.preorden(), ["gato", "casa", "perro"])
verificar("1. postorden", a.postorden(), ["casa", "perro", "gato"])

# Caso 2: orden alfabético (con acento)
a = construir_arbol("zorro árbol abeja")
verificar("2. inorden con acento", a.inorden(), ["abeja", "árbol", "zorro"])

# Caso 3: una sola palabra
a = construir_arbol("hola")
verificar("3. un nodo", a.total_nodos(), 1)
verificar("3. sin internos", a.nodos_internos(), [])
verificar("3. raíz es hoja", a.hojas(), ["hola"])

# Caso 4: duplicados (no se duplican nodos, se cuenta frecuencia)
a = construir_arbol("sol luna sol sol")
verificar("4. nodos únicos", a.total_nodos(), 2)
verificar("4. frecuencia de 'sol'", a.raiz.frecuencia, 3)

# Caso 5: conteo de nodos
a = construir_arbol("uno dos tres cuatro cinco")
verificar("5. total de nodos", a.total_nodos(), 5)

# Caso 6: varios niveles, internos y hojas
#        m
#       / \
#      c   t
#     / \
#    a   d
a = construir_arbol("m c t a d")
verificar("6. internos", sorted(a.nodos_internos()), ["c", "m"])
verificar("6. hojas", sorted(a.hojas()), ["a", "d", "t"])
verificar("6. palabra máxima", a.palabra_maxima(), "t")

# Caso 7: mayúsculas
a = construir_arbol("Gato GATO gato")
verificar("7. normalización", a.total_nodos(), 1)
verificar("7. frecuencia", a.raiz.frecuencia, 3)

# Caso 8: signos de puntuación
a = construir_arbol("¡Hola, mundo! ¿Cómo estás?")
verificar("8. limpieza", a.inorden(), ["cómo", "estás", "hola", "mundo"])

# ---- Casos límite extra ----
a = construir_arbol("")
verificar("L1. cadena vacía", a.total_nodos(), 0)
verificar("L1. máximo en árbol vacío", a.palabra_maxima(), None)

a = construir_arbol("   ,,, !!! 123 ")
verificar("L2. solo símbolos/números", a.total_nodos(), 0)

a = construir_arbol("a b c d e f")
verificar("L3. árbol degenerado (lista)", a.total_nodos(), 6)
verificar("L3. una sola hoja", a.hojas(), ["f"])

a = construir_arbol("hola   mundo\tcruel")
verificar("L4. espacios/tabs múltiples", a.total_nodos(), 3)

print(f"\n{sum(resultados)}/{len(resultados)} pruebas pasaron")
