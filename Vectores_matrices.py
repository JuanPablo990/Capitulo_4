# Juan Pablo Nieto Cortes CNYT Lab2
import libreria_complejos as lab1
from tkinter import messagebox
import math
import numpy as np

#1. Adición de vectores complejos.
def suma_Vector(a, b):
    if len(a) != len(b):
        messagebox.showerror("ERROR!", "Los vectores no pueden ser operados, no son de igual dimension")
    else:
        rtaVector = [[None for fila in range(1)] for column in range(len(a))]
        fila = len(a)
        for i in range(fila):
            rtaVector[i][0] = lab1.suma(a[i][0], b[i][0])
        return rtaVector

#1.2. Resta de vectores complejos.
def resta_Vector(a, b):
    if len(a) != len(b):
        messagebox.showerror("ERROR!", "Los vectores no pueden ser operados, no son de igual dimension")
    else:
        rtaVector = [[None for fila in range(1)] for column in range(len(a))]
        fila = len(a)
        for i in range(fila):
            rtaVector[i][0] = lab1.resta(a[i][0], b[i][0])
        return rtaVector

#2. Inverso (aditivo) de un vector complejos.
def inversoAditivo_Vector(a):
    rtaVector = [[None for fila in range(1)] for column in range(len(a))]
    fila = len(a)
    for i in range(fila):
        rtaVector[i][0] = lab1.producto(a[i][0], [-1, 0])
    return rtaVector

#3. Multiplicación de un escalar por un vector complejo.
def productoEscalar_Vector(a, b):
    fila = len(a)
    rta = [[None for column in range(len(a[0]))] for row in range(len(a))]
    for i in range(fila):
        rta[i][0] = lab1.producto(a[i][0], b)
    return rta

#4. Adición de matrices complejas.
def suma_Matriz(a, b):
    fila = len(a)
    columna = len(a[0])
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        messagebox.showerror("ERROR!", "Los matrices pueden ser operadas, no son de igual dimension")
    else:
        rtaMatriz = [[None for column in range(columna)] for row in range(fila)]

        for i in range(fila):
            for j in range(columna):
                rtaMatriz[i][j] = lab1.suma(a[i][j], b[i][j])
        return rtaMatriz

#5. Inversa (aditiva) de una matriz compleja.
def inversoAditivo_Matriz(a):
    fila = len(a)
    columna = len(a[0])
    for i in range(fila):
        for j in range(columna):
            a[i][j] = lab1.producto(a[i][j], [-1, 0])
    return a

#6. Multiplicación de un escalar por una matriz compleja.
def productoEscalar_Matriz(a, b):
    fila = len(a)
    columna = len(a[0])
    rta = [[None for column in range(columna)] for row in range(fila)]
    for i in range(fila):
        for j in range(columna):
            rta[i][j] = lab1.producto(a[i][j], b)
    return rta

#7. Transpuesta de una matriz/vector
def transpuesta_Matriz_Vector(a):
    fila = len(a)
    columna = len(a[0])
    transpuesta = [[None for column in range(fila)] for row in range(columna)]
    for i in range(fila):
        for j in range(columna):
            transpuesta[j][i] = a[i][j]
    return transpuesta

#8. Conjugada de una matriz/vector
def conjugado_Matriz_Vector(a):
    fila = len(a)
    columna = len(a[0])
    rta = [[None for j in range(columna)] for i in range(fila)]
    if columna > 1:
        for i in range(fila):
            for j in range(columna):
                rta[i][j] = lab1.conjugado(a[i][j])
    else:
        for i in range(fila):
            rta[i][0] = lab1.conjugado(a[i][0])
    return rta

#9. Adjunta (daga) de una matriz/vector
def adjunta_Matriz_Vector(a):
    conj = a[:]
    newConj = conjugado_Matriz_Vector(conj)
    trans = transpuesta_Matriz_Vector(newConj)
    return trans

#10. Producto de dos matrices (de tamaños compatibles)
def producto_Matriz(a, b):
    filaA = len(a)
    filaB = len(b)
    columnaA = len(a[0])
    columnaB = len(b[0])
    if columnaA != filaB:
        messagebox.showerror("ERROR!", "Los matrices pueden ser operadas, no son compatibles")
    else:
        rta = [[[0, 0] for columna in range(columnaB)] for fila in range(filaA)]

        for i in range(filaA):
            for j in range(columnaB):
                for k in range(filaB):
                    rta[i][j] = lab1.suma(rta[i][j], lab1.producto(a[i][k], b[k][j]))
        return rta

#11. Función para calcular la "acción" de una matriz sobre un vector.
def accion_MatrizSobreVector(a, b):
    return producto_Matriz(a, b)

#12. Producto interno de dos vectores
def productoInterno_Vector(a, b):
    newVector = adjunta_Matriz_Vector(a)
    return producto_Matriz(newVector, b)

#13. Norma de un vector
def normaVector(a):
    fila = len(a)
    columna = len(a[0])
    rta = 0
    for i in range(fila):
        for j in range(columna):
            rta += a[i][j][0] ** 2 + a[i][j][1] ** 2
    return math.sqrt(rta)

#14. Distancia entre dos vectores
def distanciaVector(a, b):
    resta = resta_Vector(a, b)
    norma = normaVector(resta)
    return norma
#15.Valores  y vectores propios de una matriz
#valores propios de una matriz
def Valores_propios(v1):
    mat = np.array(v1)
    eigenvalue, featurevector = np.linalg.eig(mat)
    return eigenvalue
#vectores propios de una matriz
def vectores_propios(v1):
    mat = np.array(v1)
    eigenvalue, featurevector = np.linalg.eig(mat)
    return featurevector

#16. Revisar si una matriz es unitaria
def matrizUnitaria(a):
    daga = adjunta_Matriz_Vector(a)
    operacion = producto_Matriz(a, daga)
    fila = len(a)
    columna = len(a[0])
    matrizIdentidad = [[[1, 0] if x == y else [0, 0] for y in range(columna)] for x in range(fila)]
    for i in range(fila):
        for j in range(columna):
            operacion[i][j] = [round(operacion[i][j][0]), round(operacion[i][j][1])]
    if operacion == matrizIdentidad:
        return True
    else:
        return False

#17. Revisar si una matriz es Hermitiana
def matrizHermitiana(a):
    daga = adjuntaMatrizVector(a)
    if daga == a:
        return True
    else:
        return False

#18. Producto tensor de dos matrices/vectores
def productoTensorial_Matriz_Vector(a, b):
    filaM1, filaM2 = len(a), len(b)
    columnaM1, columnaM2 = len(a[0]), len(b[0])
    nuevaMatriz = [[[0, 0] for column in range(columnaM1 * columnaM2)] for row in range(filaM1 * filaM2)]
    for i in range(len(nuevaMatriz)):
        for j in range(len(nuevaMatriz[0])):
            nuevaMatriz[i][j] = lab1.producto(a[i // filaM2][j // columnaM2], b[i % filaM2][j % columnaM2])
    return nuevaMatriz


""" Sistema cuántico de partícula en una linea """

def probabilidad (pos,vector):
    print(vector)
    a= norma(vector[pos])
    b=norma_vector(vector)
    prob=(a/b)
    respuesta=prob*100
    return respuesta

def amplitudTransicion(matriz,vector):
    a = vectorxmatriz(vector,matriz)
    conjugado = inversovector(a)
    respuesta = producto_vectores(conjugado,vector)
    return respuesta

