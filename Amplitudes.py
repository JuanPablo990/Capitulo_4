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

# COMPLETE LOS RETOS DE PROGRAMACIÓN DEL CAPÍTULO 4.
#1. Amplitud de transición. El sistema puede recibir dos vectores y calcular la probabilidad de transitar de el uno al otro después de hacer la observación

def amplitud_transicion(v1,v2):
    produc = vc.productoInterno_Vector(v1,v2)
    resultado = lc.division(produc[0][0][0],((vc.normaVector(v1))*(vc.normaVector(v2))))
    return resultado
def ParticulaPosicion(ket,X):
    return lc.detectarParticula(ket,X)
def transitarVectorVector(ket,ket2):

    return lc.transitarVector(ket,ket2)
def valorEsperado(obs,ket):
    obsSobreket = lc.accion(obs, ket)
    bra = lc.matrizConjugada(obsSobreket)
    ket1 = lc.transpuesta([ket])
    bra1 = lc.transpuesta(bra)
    car = lc.multiplicacionMatrizMatriz(bra1, ket1)[0][0]
    return car

# 2. Ahora con una matriz que describa un observable y un vector ket, el sistema revisa que la matriz sea hermitiana, y si lo es, calcula la media y la varianza del observable en el estado dado.

def varianza(M, v):
    if len(M) == len(v[0]):
        H = lc.multmat(M, lc.trama(v))
        w = [[]]
        for j in H:
            w[0].append(j[0])
        x = lc.multmat(lc.trama(w), v)
        E = x[0][0][0] + x[1][0][1]
        m1 = lc.ident(E, M)
        N = lc.cplxrest(M, m1)
        Delta = lc.multmat(N, N)
        r = v
        for i in range(len(v)):
            for j in range(len(v[0])):
                x = v[i][j]
                c = x[0] ** 2
                t = x[1] ** 2
                r[i][j] = (c, t)
        Rf = lc.multmat(r, Delta)
        x = lc.prm(Rf[0][0])
        return round(x[0], 1)

def varianzaObservable(obs,ket):
    nve = lc.multiplicacion(valorEsperado(obs, ket), (-1, 0))
    mve = lc.multiplicacionEscalarMatriz(lc.matrizIdentidad(len(obs)), nve)
    delta = lc.sumaMatrices(obs, mve)
    deltaCuadrado = lc.multiplicacionMatrizMatriz(delta, delta)
    var = valorEsperado(deltaCuadrado, ket)


# 3. El sistema calcula los valores propios del observable y la probabilidad de que el sistema transite a alguno de los vectores propios después de la observación.

def estadospropios(ob, v):
    ob1 = []
    for i in range(len(ob)):
        ob1.append([])
        for j in range(len(ob[0])):
            ob1[i].append(ob[i][j])
    for i in range(len(ob1)):
        for j in range(len(ob1[0])):
            ob1[i][j] = lc.complejo(ob1[i][j])
    N = list(ob1[0])
    y = varianza(ob, v)
    return N, y

def propiosObservable(obs):
    for i in range(len(obs)):
        for j in range(len(obs[0])):
            obs[i][j]=complex(obs[i][j][0],obs[i][j][1])
    return obs

def probabilidadObservable(obs,ket):

    valP,vectP = propiosObservable(obs)
    probs=[]
    for v in vectP:
        p = vc.transitarVector(v,ket)
        probs.append(p)
    return probs

def detectarParticula(ket,X):
    normaKet=lc.normaMatriz([ket])
    normaComplejo=lc.normaMatriz([[ket[X]]])
    return (normaComplejo**2)/(normaKet**2)
def transitarVector(ket,ket2):
    ket1=lc.transpuesta([ket])
    bra=lc.matrizConjugada([ket2])
    car=lc.multiplicacionMatrizMatriz(bra,ket1)[0][0]
    normaBra=lc.normaMatriz(bra)
    normaket=lc.normaMatriz(ket1)
    car2=(normaBra*normaket,0)
    return lc.division(car,car2)

# 4. Se considera la dinámica del sistema. Ahora con una serie de matrices Un el sistema calcula el estado final a partir de un estado inicial.

def dinamica(un,init,steps):
    up=[un]
    ur=un
    for p in range(steps):
        ur=vc.producto_Matriz(ur,ur)
        up.append(ur)
    un1=[]
    for k in range(len(up)):
        un1=vc.producto_Matriz(up[k],up[k-1])
    temp=lc.accion(un1,init)
    return temp67763
