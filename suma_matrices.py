#!/usr/bin/env python
# -*- coding: utf-8 -*-

print("Programa que suma dos matrices")
print("------------------------------\n")
filas = int(input("Ingrese la cantidad de filas: "))
columnas = int(input("Ingrese la cantidad de columnas: "))
matriz_A, matriz_B, matriz_suma = [], [], []
for fila in range(filas):
      matriz_A.append([0] * columnas)
      matriz_B.append([0] * columnas)
      matriz_suma.append([0] * columnas)


print("Ingrese los elementos de la primera matriz:")
for i in range(filas):
      for j in range(columnas):
            matriz_A[i][j] = float(input("matriz_A[{}][{}]= ".format(i, j)))
            
print("Ingrese los elementos de la segunda matriz:")
for i in range(filas):
      for j in range(columnas):
            matriz_B[i][j] = float(input("matriz_B[{}][{}]= ".format(i,j)))
            
for i in range(filas):
      for j in range(columnas):
            matriz_suma[i][j] = matriz_A[i][j] + matriz_B[i][j]

print("La matriz suma es :")
for i in range(filas):
      print(matriz_suma[i])
