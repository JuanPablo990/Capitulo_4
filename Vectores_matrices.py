# Juan Pablo Nieto Cortes CNYT Lab2
import libreria_complejos as lab1
from tkinter import messagebox
import math
import numpy as np

def sumavector(vector1, vector2):
    vectorfinal = []
    if len(vector1) == len(vector2):
        for i in range(len(vector1)):
            vectorfinal.append(sumar(vector1[i], vector2[i]))
    return vectorfinal


def inversovector(vector1):
    vectorfinal = []
    for i in range(len(vector1)):
        vectorfinal.append(conjugado(vector1[i]))
    return vectorfinal


def producto_vectores(vector1, vector2):
    resultado = (0, 0)
    for i in range(len(vector1)):
        resultado = sumar(resultado, multiplicar(vector1[i], vector2[i]))
    return resultado


def producto_vectoresReales(vector1, vector2):
    resultado = 0
    for i in range(len(vector1)):
        resultado += vector1[i] * ector2[i]
    return resultado


def producto_interno(vector1, vector2):
    return producto_vectores((conjugada_vector(vector1)), vector2)


def escalar_vector(numero, vector1):
    operacion = []
    for i in vector1:
        resultado = multiplicar(numero, i)
        operacion.append(resultado)
    return operacion


def adicion_matrices(matriz1, matriz2):
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2):
        print("La suma no esta definida para matrices de diferente tamaño")
    else:
        resultado = []
        for i in range(len(matriz1)):
            operacion = []
            for j in range(len(matriz2)):
                operacion.append(sumar(matriz1[i][j], matriz2[i][j]))
            resultado.append(operacion)
        return resultado


def matriz_inversa(matriz1):
    resultado = []
    for i in range(len(matriz1)):
        resultado.append(inversovector(matriz1[i]))
    return resultado


def escalar_matriz(numero, matriz1):
    resultado = []
    for i in range(len(matriz1)):
        operacion = []
        for j in range(len(matriz1)):
            operacion.append(multiplicar(numero, matriz1[i][j]))
        resultado.append(operacion)
    return resultado


def transpuesta_matriz(matriz1):
    matriz = [0] * len(matriz1[0])
    for i in range(len(matriz1)):
        matriz[i] = [0] * len(matriz1)
        for j in range(len(matriz1[i])):
            matriz[i][j] = matriz1[j][i]
    return matriz


def transpuesta_vector(vector1):
    return vector1


def conjugada_matriz(matriz1):
    resultado = []
    for i in range(len(matriz1)):
        operacion = []
        for j in range(len(matriz1)):
            operacion.append(conjugado(matriz1[i][j]))
        resultado.append(operacion)
    return resultado


def conjugada_vector(vector1):
    resultado = []
    for i in vector1:
        resultado.append(conjugado(i))
    return resultado


def adjunta_matriz(matriz1):
    return transpuesta_matriz(conjugada_matriz(matriz1))


def adjunta_vector(vector1):
    return conjugada_vector(vector1)


def producto_matrices(matriz1, matriz2):
    resultado = []
    for i in range(len(matriz1)):
        operacion = []
        for j in range(len(matriz2[0])):
            save = (0, 0)
            for k in range(len(matriz2)):
                save = sumar(multiplicar(matriz1[i][k], matriz2[k][j]), save)
            operacion.append(save)
        resultado.append(operacion)
    return resultado


def producto_matrices_reales(matriz1, matriz2):
    resultado = []
    for i in range(len(matriz1)):
        fila = []
        for j in range(len(matriz2[0])):
            save = 0
            for k in range(len(matriz2)):
                multi = matriz1[i][k] * matriz2[k][j]
                save += multi
            fila.append(save)
        resultado.append(fila)
    return resultado


def norma(numero1):
    return (numero1[0] ** 2 + numero1[1] ** 2)


def norma_vector(vectorreal1):
    resultado = 0
    for i in vectorreal1:
        resultado = resultado + norma(i)
    return resultado


def distancia_vectores(vectorreal1, vectorreal2):
    resultado = ((vectorreal1[0] - vectorreal2[0]) ** 2 + (vectorreal1[1] - vectorreal2[1]) ** 2) ** 0.5
    return resultado


def matriz_unitaria(matriz1):
    resultado = producto_matrices(matriz1, adjunta_matriz(matriz1))
    for i in range(len(matriz1)):
        for j in range(len(matriz1[0])):
            posicion = resultado[i][j]
            if (i == j and (posicion[0] != 1 or posicion[1] != 0)):
                return False
            elif (i != j and (posicion[0] != 0 or posicion[1] != 0)):
                return False
    return True


def matriz_hermitiana(matriz1):
    for i in range(len(matriz1)):
        for j in range(len(matriz1[0])):
            if (matriz1[i][j] != adjunta_matriz(matriz1)[i][j]):
                return False
    return True


def producto_tensor_vectores(vector1, vector2):
    operacion = []
    for i in vector1:
        numero = i
        for j in vector2:
            numero2 = j
            resultado = multiplicar(numero, numero2)
            operacion.append(resultado)
    return operacion


def producto_tensor_matrices(matriz1, matriz2):
    operacion = []
    for i in range(len(matriz1)):
        for j in range(len(matriz2)):
            operacion.append(producto_tensor_vectores(matriz1[i], matriz2[j]))
    return operacion


def vectorxmatriz(vector, matriz):
    ans = []
    for i in range(len(matriz)):
        ans.append(producto_vectores(vector, matriz[i]))
    return ans


def vectormatrizReal(vector, matriz):
    resultado = []
    for i in range(len(matriz)):
        resultado.append(producto_vectoresReales(vector, matriz[i]))
    return resultado


"Sistema cuántico de partícula en una linea"


def probabilidad(pos, vector):
    print(vector)
    a = norma(vector[pos])
    b = norma_vector(vector)
    prob = (a / b)
    respuesta = prob * 100
    return respuesta


def amplitudTransicion(matriz, vector):
    a = vectorxmatriz(vector, matriz)
    conjugado = inversovector(a)
    respuesta = producto_vectores(conjugado, vector)
    return respuesta