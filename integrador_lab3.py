#!/usr/bin/env python
# -*- coding: utf-8 -*-

print("\nPrograma de administración de alumnos")
print("-------------------------------------")
nombre = input("Ingrese el nombre del alumno: ")
cursos = int(input("Ingrese la cantidad de cursos: "))
alumno = (nombre, cursos)
alumnos = []
alumnos.append(alumno)
opcion = 0
while opcion != 3:
        print("\nMenú principal")
        print("--------------")
        print("1 - Ver la lista de alumnos.")
        print("2 - Añadir un alumno a la lista.")
        print("3 - Salir.")
        opcion = int(input("Ingrese el número de la operación que desea ejecutar: "))
        if opcion == 1:
                print("Lista de alumnos:")
                for i in range(len(alumnos)):
                        print(alumnos[i])
                continue
        elif opcion == 2:
                nombre = input("Ingrese el nombre del alumno: ")
                cursos = int(input("Ingrese la cantidad de cursos: "))
                alumno = [nombre, cursos]
                alumnos.append(alumno)
                continue
        elif opcion == 3:
                print("¡Gracias por utilizar el programa!")
                break
        else:
                print("La opción ingresada no es correcta, vuelva  a intentarlo.")
                
                
