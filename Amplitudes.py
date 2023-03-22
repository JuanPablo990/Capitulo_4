# Juan Pablo Nieto Cortes
import libreria_complejos as lc
import Vectores_matrices as vc
import math

# SIMULE EL PRIMER SISTEMA CUÁNTICO DESCRITO EN LA SECCIÓN 4.1.
# 1. Probabilidad de observación
"""
v1 es un vector cualquiera y a es la posicion en el que se busca la probabilidad
"""
def probabilidad (v1,a):
    resultado = ((lc.modulo(v1[a][0]))**2 )/(vc.normaVector(v1)**2)
    return resultado

# 2. El sistema si se le da otro vector Ket debe buscar la probabilidad de transitar del primer vector al segundo.
"""
v1 es un vector donde queremos llegar y v2 es el vector donde iniciamos
"""
def probabilidad_transicion(v1,v2):
    # normalizar los vectores
    vn1= vc.productoEscalar_Vector(v1,(1/vc.normaVector(v1),0))
    vn2 = vc.productoEscalar_Vector(v2, (1 / vc.normaVector(v2), 0))
    resultado = vc.productoInterno_Vector(vn1,vn2)
    return resultado

# COMPLETE LOS RETOS DE PROGRAMACIÓN DEL CAPÍTULO 4.
#1. Amplitud de transición. El sistema puede recibir dos vectores y calcular la probabilidad de transitar de el uno al otro después de hacer la observación

v1 = [[[1,0]],[[0,-1]]]
v2= [[[0,1]],[[1,0]]]
def amplitud_transicion(v1,v2):
    produc = vc.productoInterno_Vector(v1,v2)
    resultado = 1#lc.division(produc[0][0][0],((vc.normaVector(v1))*(vc.normaVector(v2))))
    print(produc)
    print(vc.normaVector(v1)*vc.normaVector(v2))
    return resultado

if __name__ == "__main__":
    print(amplitud_transicion(v1,v2))