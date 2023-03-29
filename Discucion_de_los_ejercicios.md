# 4.5.2 y 4.5.3

Postulate 4.5.1 Assume we have two independent quantum systems Q and Q , represented respectively by the vector spaces V and V . The quantum system obtained by merging Qand Q will have the tensor product V ⊗ V as a state space.

# Analisis:
Sabiendo que el producto tensor es asociativo , se puede inferir que cada uno de los vectores V representara un sistema largo de varios proodctos tensores entre si , por lo cual siguiendo el postulado , se toma el conjunto de complejos y se busca su probabilidad en un punto especifico dado:

siendo m = n =4 con complejos Co,o=...=C3.3=1+i , buscamos la particula en el punto X1:
	
	n= matriz([ [[1,1]],[[1,1]],[[1,1]],[[1,1]],[[1,1]],[[1,1]],[[1,1]],[[1,1]],[[1,1]],[[1,1]],[[1,1]],[[1,1]],[[1,1]],[[1,1]],[[1,1]],[[1,1]] ])
	###Hallamos modulo cuadrado a cada uno de los complejos del vector
	for i in range(len(n.c)):
		n.c[i][0]=n.c[i][0].modulo_cuadrado()
  
Luego verificamos cual es la probabilidad de enconttrar una particula de posicion x1 y otra particula en una posicion y1 :

	>>> x_position= n.c[1][0]
	# con la posicion x1 y y1 procedemos a calcular la probabilidad dividiendolo bajo la suma de  todos los complejos tenidos del vector anteriormente.
	>>> cont=0
	>>> for i in range(len(n.c)):
		cont+=n.c[i][0]
	>>> print(x_position[0]/cont)
	0.0625

En terminos probabillisticos , esta cantidad es suficientemente grande con un valor del 62.5% de que esten ambas particulas en estas dos posiciones.
