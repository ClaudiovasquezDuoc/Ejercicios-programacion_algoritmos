import numpy as np


matriz = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])

print("Ingresa los valores de la matriz 3x3:")
for i in range(3):
  for j in range(3):
    matriz[i, j] = int(input(f"Valor para la posición [{i}, {j}]: "))

suma_actual = np.sum(matriz)

diferencia = 21 - suma_actual

matriz[0, 0] = matriz[0, 0] + diferencia

print("Matriz resultante:")
print(matriz)
print("Suma de los elementos:", np.sum(matriz))
