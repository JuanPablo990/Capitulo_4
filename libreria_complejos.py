# Juan Pablo Nieto Cortes CNYT LAB1
import math

# Suma
def suma(c1, c2):
    return [c1[0] + c2[0], c1[1] + c2[1]]


# Producto
def producto(c1, c2):
    real = c1[0] * c2[0] - c1[1] * c2[1]
    imaginario = c1[0] * c2[1] + c1[1] * c2[0]
    return [real, imaginario]

# Resta
def resta(c1, c2):
    return [c1[0] - c2[0], c1[1] - c2[1]]

# División
def division(c1, c2):
    num = producto(c1, conjugado(c2))
    denomi = producto(c2, conjugado(c2))
    real = num[0] / denomi[0]
    imaginario = num[1] / denomi[0]
    return [real, imaginario]

# Módulo
def modulo(c1):
    return math.sqrt(c1[0]**2 + c1[1]**2)

# Conjugado
def conjugado(c1):
    return [c1[0], c1[1]*-1]

#Conversión entre representaciones polar y cartesiano
# cartesianas a polares
def cart_pol(c1):
    r = math.sqrt(c1[0]**2 + c1[1]**2)
    angle = math.degrees(math.atan2(c1[1], c1[0]))
    return [r, angle]

# polares a cartesianas
def pol_cart(c1):
    r, angle = c1[0], math.radians(c1[1])
    x = r * math.cos(angle)
    y = r * math.sin(angle)
    return [x, y]

#Retornar la fase de un número complejo.
def fase(c1):
    return math.degrees(math.atan2(c1[1], c1[0]))