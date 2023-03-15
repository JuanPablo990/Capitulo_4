# Juan Pablo Nieto Cortes
import libreria_complejos as lc
import Vectores_matrices as vc
import math
v1 = [[[-3,-1]],[[0,-2]],[[0,1]],[[2,0]]]
# Probabilidad de observación
def probabilidad (v1,a):
    resultado = ((lc.modulo(v1[a][0]))**2 )/(vc.normaVector(v1)**2)
    return resultado

if __name__ == '__main__':
    print(probabilidad(v1,2))