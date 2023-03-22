# Juan Pablo Nieto Cortes
import libreria_complejos as lc
import Vectores_matrices as vc
import math

# SIMULE EL PRIMER SISTEMA CUÁNTICO DESCRITO EN LA SECCIÓN 4.1.
# 1. Probabilidad de observación
def probabilidad (v1,a):
    resultado = ((lc.modulo(v1[a][0]))**2 )/(vc.normaVector(v1)**2)
    return resultado

# 2. El sistema si se le da otro vector Ket debe buscar la probabilidad de transitar del primer vector al segundo.
def probabilidad_transicion(v1,v2):
    # normalizar los vectores
    vn1= vc.productoEscalar_Vector(v1,(1/vc.normaVector(v1),0))
    vn2 = vc.productoEscalar_Vector(v2, (1 / vc.normaVector(v2), 0))
    resultado = vc.productoInterno_Vector(vn1,vn2)
    return resultado


if __name__ == "__main__":
    print(probabilidad_transicion(v1,v2))