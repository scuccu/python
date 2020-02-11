#!/usr/bin/env python
# -*- coding: utf-8 -*-


temperatura=float(input("Ingrese la temperatura en grados centigrados"))
escala=input( 'C' " para Celcius o" 'F' " para farenheit")

if escala == "C" or escala == "c" :
	valor=(9/5)* temperatura+32
	print( " la escala es:" +str(valor) +"ºF")
elif escala == "F" or escala == "f" :
	valor= temperatura-32 *5/9
	print( " la escala es:" +str(valor) +"ºC")
else:
	print("ingrese una letra correcta")


cadena1=input("Ingrese cadena1: ")
cadena2=input("Ingrese cadena2: ")

if cadena1 == cadena2:
	print("Bien!")
else:
	print("Mal")

nombre= input("Ingrese su nombre: ")

if nombre == "":
	print("El renglon esta vacio")
else:
	print("Correcto")



print (5 == 6)

a= int(5)

print (type(a))

print(a != 5.0)  # no es recomendable comparar entre distintos tipos ya que puede generar confusiòn

print ((5>6 and 3<4) or (a == 5))

calle= input ("Ingrese el nomnre de la calle: ")
nro= input ("Ingrese la altura: ")
edad = input("Ingrese su edad: ")
edad = int(edad)
print("Su direcciòin y su edad son: " +calle+ " " +str(nro))

if 20 > edad >=16:
	print("Usted esta habilitado para votar")
elif edad > 20:
	print("Usted puede votar con libreta")
else :
	print ("Usted no esta habilidado para votar")
	
	
	
	




