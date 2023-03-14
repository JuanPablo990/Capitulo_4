# Juan Pablo Nieto Cortes
import libreria_complejos as lc
import Vectores_matrices as vc
import math
v1 = [[-3,-1],[0,-2],[0,1],[2,0]]
def amplitudes_complejas (v1):
    resultado = vc.normaV(v1)
    print(v1)
    return resultado

if __name__ == '__main__':
    amplitudes_complejas(v1)