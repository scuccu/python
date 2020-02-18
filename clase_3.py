#!/usr/bin/env python
# -*- coding: utf-8 -*-

listado= [1,2,3,'pepe',True]
#listado.append(22)
print(listado[3])
listado.insert(3,'jose')    #pongo la posicion y lo que quiero poner
print(listado)
del listado[-1] 
print(listado)

n=listado.index('pepe')
listado.insert(n+1,'argento')  #guardo la posicion en una variable y puedo usarla de referencia
print(listado)


i=0
while i<10:
	print(i,end=' ')
	i=i+1
	
a=1	
while True:
	if a < 5:
		print("Hola mundo")
		a=a+1
	else:
		break		
	
mi_lista=[[3.14,"Hola mundo"], [True, False, -5]]
print(mi_lista)
print(mi_lista[1])
print(mi_lista [1][2])  #imprimo de la lista 1 el componente 2 //concepto de matriz

alumnos =["Matias" , "Jorge" , "Marta" , "Pablo"]
for alumno in alumnos:    #siempre la i va en singular y la iteracionn en plural
	print(alumno)
	#print(type(alumno))
	
saludo = list("Hola mundo")
for letra in saludo:
	print(letra)
	
alumnos =["Matias" , "Jorge" , "Marta" , "Pablo"]
notas =[10,6,7,8]
for indice in range(4):   #4 es la cantidad de elementos que toma la seleccion
#for indice in range(2,4): Me pongo en la posiciòn 2 (Marta) y recorro desde ahi
	print(alumnos[indice], notas[indice])


matriz=[[2.1,3.4,5.8],[9.2,6.7,8.5]]
print(matriz)
posicion1=int(input("Diga primera posiciòn: "))
posicion2=int(input("Diga segunda posiciòn: "))
if posicion1 =>2 and posicion2 =>3:
	print("ingrese 0 o 1")
else:
print(matriz[posicion1][posicion2])

flag = 'f'
while flag != 'q':	
matriz=[[2.1,3.4,5.8],[9.2,6.7,8.5]]
fila= input("ingrese el numero de fila: ")
columna= input("Ingrese el numero de columna: ")
if fila!='0' and fila !='1':
	print("Error en fila")
elif columna != '0' and columna != '1' and columna != '2':
	print("Error en columna")
else:
	print(matriz[int(fila)] [int(columna)])
	
flag = input(" f para seguir, q para terminar")
