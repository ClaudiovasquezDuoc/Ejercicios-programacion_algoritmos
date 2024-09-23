import numpy as np
matriz1= np.array([[1,0,0],[0,2,0],[0,0,3]])
matriz2= np.array([[1,0,0],[0,2,0],[0,0,3]])
nueva_matriz = np.array([
    [matriz1[0, 0], matriz1[1, 1]],
    [matriz2[1, 0], matriz2[1, 1]]
])
print(nueva_matriz)
