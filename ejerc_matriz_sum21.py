import numpy as np

matriz = np.array([[5, 6, 0], [0, 5, 0], [0, 0, 1]])

suma_actual = np.sum(matriz)

diferencia = 21 - suma_actual

matriz[0, 2] = matriz[0, 2] + diferencia

print(matriz)
print(np.sum(matriz))
