"""
Árbol Binario de Búsqueda (ABB) de palabras.

Recibe una oración, la limpia, separa sus palabras y las guarda en un ABB.
Luego muestra recorridos, conteos, palabra máxima, hojas e internos.

DECISIONES DE DISEÑO (documentadas):
1. Duplicados: NO se insertan de nuevo; en su lugar se incrementa el
   contador "frecuencia" del nodo existente. Así el árbol solo tiene
   palabras únicas pero no perdemos cuántas veces apareció cada una.
2. Normalización: todo se pasa a minúsculas y se quitan los signos de
   puntuación (se conservan letras, acentos y la ñ).
3. Orden alfabético: para comparar se ignoran los acentos, de modo que
   "árbol" se ubique junto a "abeja" y no después de "zorro".
"""

import re
import unicodedata


# ---------------------------------------------------------------------------
# Utilidades de texto
# ---------------------------------------------------------------------------
def limpiar_y_dividir(oracion):
    """Convierte la oración a minúsculas y devuelve la lista de palabras
    sin signos de puntuación."""
    oracion = oracion.lower()
    # \w = letras/números/guion bajo (incluye acentos y ñ en Python 3)
    palabras = re.findall(r"[^\W\d_]+", oracion)
    return palabras


def clave_orden(palabra):
    """Clave usada para comparar: la palabra sin acentos.
    Ej: 'árbol' -> 'arbol'."""
    descompuesta = unicodedata.normalize("NFD", palabra)
    return "".join(c for c in descompuesta if unicodedata.category(c) != "Mn")


# ---------------------------------------------------------------------------
# Estructura del árbol
# ---------------------------------------------------------------------------
class Nodo:
    def __init__(self, palabra):
        self.palabra = palabra
        self.frecuencia = 1      # veces que apareció la palabra
        self.izquierdo = None
        self.derecho = None

    def es_hoja(self):
        return self.izquierdo is None and self.derecho is None


class ArbolBST:
    def __init__(self):
        self.raiz = None

    # ----- Inserción -------------------------------------------------------
    def insertar(self, palabra):
        self.raiz = self._insertar(self.raiz, palabra)

    def _insertar(self, nodo, palabra):
        if nodo is None:
            return Nodo(palabra)

        clave_nueva = clave_orden(palabra)
        clave_actual = clave_orden(nodo.palabra)

        if clave_nueva < clave_actual:
            nodo.izquierdo = self._insertar(nodo.izquierdo, palabra)
        elif clave_nueva > clave_actual:
            nodo.derecho = self._insertar(nodo.derecho, palabra)
        else:
            nodo.frecuencia += 1   # duplicado: solo se cuenta
        return nodo

    # ----- Recorridos ------------------------------------------------------
    def inorden(self):
        resultado = []
        self._inorden(self.raiz, resultado)
        return resultado

    def _inorden(self, nodo, lista):
        if nodo:
            self._inorden(nodo.izquierdo, lista)
            lista.append(nodo.palabra)
            self._inorden(nodo.derecho, lista)

    def preorden(self):
        resultado = []
        self._preorden(self.raiz, resultado)
        return resultado

    def _preorden(self, nodo, lista):
        if nodo:
            lista.append(nodo.palabra)
            self._preorden(nodo.izquierdo, lista)
            self._preorden(nodo.derecho, lista)

    def postorden(self):
        resultado = []
        self._postorden(self.raiz, resultado)
        return resultado

    def _postorden(self, nodo, lista):
        if nodo:
            self._postorden(nodo.izquierdo, lista)
            self._postorden(nodo.derecho, lista)
            lista.append(nodo.palabra)

    # ----- Conteos ---------------------------------------------------------
    def total_nodos(self):
        return self._total(self.raiz)

    def _total(self, nodo):
        if nodo is None:
            return 0
        return 1 + self._total(nodo.izquierdo) + self._total(nodo.derecho)

    def nodos_internos(self):
        """Lista de palabras de nodos con al menos un hijo."""
        resultado = []
        self._internos(self.raiz, resultado)
        return resultado

    def _internos(self, nodo, lista):
        if nodo:
            if not nodo.es_hoja():
                lista.append(nodo.palabra)
            self._internos(nodo.izquierdo, lista)
            self._internos(nodo.derecho, lista)

    def hojas(self):
        """Lista de palabras de nodos sin hijos."""
        resultado = []
        self._hojas(self.raiz, resultado)
        return resultado

    def _hojas(self, nodo, lista):
        if nodo:
            if nodo.es_hoja():
                lista.append(nodo.palabra)
            self._hojas(nodo.izquierdo, lista)
            self._hojas(nodo.derecho, lista)

    def palabra_maxima(self):
        """La mayor alfabéticamente es el nodo más a la derecha."""
        if self.raiz is None:
            return None
        actual = self.raiz
        while actual.derecho:
            actual = actual.derecho
        return actual.palabra

    # ----- Representación visual ------------------------------------------
    def dibujar(self):
        """Devuelve el árbol como texto, girado 90° (derecha arriba,
        izquierda abajo, la raíz a la izquierda)."""
        lineas = []
        self._dibujar(self.raiz, 0, lineas)
        return "\n".join(lineas)

    def _dibujar(self, nodo, nivel, lineas):
        if nodo:
            self._dibujar(nodo.derecho, nivel + 1, lineas)
            extra = f" (x{nodo.frecuencia})" if nodo.frecuencia > 1 else ""
            lineas.append("      " * nivel + nodo.palabra + extra)
            self._dibujar(nodo.izquierdo, nivel + 1, lineas)


    def dibujar_grafico(self):
        """Devuelve el árbol en forma clásica (raíz arriba, hijos abajo)
        usando / y \\ para mostrar la estructura."""
        if self.raiz is None:
            return ""
        caja = _caja_nodo(self.raiz)[0]
        # Quitar renglones vacíos al final
        return "\n".join(l.rstrip() for l in caja if l.strip())



def _caja_nodo(nodo):
    """Dibuja recursivamente un subárbol como una 'caja' de texto.
    Devuelve (lineas, ancho, inicio_raiz, fin_raiz)."""
    if nodo is None:
        return [], 0, 0, 0

    texto = nodo.palabra + (f"({nodo.frecuencia})" if nodo.frecuencia > 1 else "")
    ancho_raiz = len(texto)
    hueco = ancho_raiz

    caja_izq, ancho_izq, ini_izq, fin_izq = _caja_nodo(nodo.izquierdo)
    caja_der, ancho_der, ini_der, fin_der = _caja_nodo(nodo.derecho)

    linea1, linea2 = [], []

    if ancho_izq > 0:
        centro_izq = (ini_izq + fin_izq) // 2 + 1
        linea1.append(" " * (centro_izq + 1))
        linea1.append("_" * (ancho_izq - centro_izq))
        linea2.append(" " * centro_izq + "/")
        linea2.append(" " * (ancho_izq - centro_izq))
        inicio_raiz = ancho_izq + 1
        hueco += 1
    else:
        inicio_raiz = 0

    linea1.append(texto)
    linea2.append(" " * ancho_raiz)

    if ancho_der > 0:
        centro_der = (ini_der + fin_der) // 2
        linea1.append("_" * centro_der)
        linea1.append(" " * (ancho_der - centro_der + 1))
        linea2.append(" " * centro_der + "\\")
        linea2.append(" " * (ancho_der - centro_der))
        hueco += 1

    fin_raiz = inicio_raiz + ancho_raiz - 1
    caja = ["".join(linea1), "".join(linea2)]

    for i in range(max(len(caja_izq), len(caja_der))):
        l = caja_izq[i] if i < len(caja_izq) else " " * ancho_izq
        r = caja_der[i] if i < len(caja_der) else " " * ancho_der
        caja.append(l + " " * hueco + r)

    return caja, len(caja[0]), inicio_raiz, fin_raiz


# ---------------------------------------------------------------------------
# Construcción y reporte
# ---------------------------------------------------------------------------
def construir_arbol(oracion):
    arbol = ArbolBST()
    for palabra in limpiar_y_dividir(oracion):
        arbol.insertar(palabra)
    return arbol


def mostrar_reporte(arbol):
    if arbol.raiz is None:
        print("No se encontraron palabras válidas en la oración.")
        return

    print("\n--- Estructura del árbol (raíz arriba) ---")
    print(arbol.dibujar_grafico())

    print("\n--- Vista alterna (raíz a la izquierda, derecha arriba) ---")
    print(arbol.dibujar())

    print("\n--- Recorridos ---")
    print("Inorden   :", arbol.inorden())
    print("Preorden  :", arbol.preorden())
    print("Postorden :", arbol.postorden())

    total = arbol.total_nodos()
    internos = arbol.nodos_internos()
    hojas = arbol.hojas()

    print("\n--- Estadísticas ---")
    print("Total de nodos     :", total)
    print("Nodos internos     :", len(internos))
    print("Palabra máxima     :", arbol.palabra_maxima())

    print("\n--- Información por tipo de nodo ---")
    print("Hojas              :", hojas)
    print("Nodos internos     :", internos)


def main():
    oracion = input("Escribe una oración: ")
    arbol = construir_arbol(oracion)
    mostrar_reporte(arbol)


if __name__ == "__main__":
    main()
