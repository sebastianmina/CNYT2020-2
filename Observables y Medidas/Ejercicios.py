import Vectores_matrices
import numpy as np

def posibilidad(vector,num):
    #Ejercicio 4.3.1
    conjunto = [[(0,1),(1,0)],
                [(0,-1),(1,0)],
                [(1,0),(1,0)],
                [(-1,0),(1,0)],
                [(0,0),(1,0)],
                [(1,0),(0,0)]]
    resultado = []
    for i in range((num*2)-2,num*2):
        if Vectores_matrices.probabilidad(vector,conjunto[i]) != 0.0:
            resultado = resultado + conjunto[i]
    return resultado

def probabilidad2(a, valor):
    #Ejercicio 4.3.2
    matrices = [[[(1,0),(0,0)],
                 [(0,0),(-1,0)]],
                [[(0,0),(0,-1)],
                 [(0,1),(0,0)]],
                [[(0,0),(1,0)],
                 [(1,0),(0,0)]]]
    arreglo = []
    posible = posibilidad(a,valor)
    arreglo2 = []
    respuesta = 0
    for i in range(3):
        valores = np.linalg.eig(matrices[i])
        arreglo = arreglo + [valores]
    for i in range(len(posible)):
        arreglo2 = arreglo2 + [posible(a, posible[i])]
    for i in range(2):
        respuesta = respuesta + (posible[i]*arreglo[valor][i])
    return respuesta

def comprueba():
    # Ejercicio 4.4.1
    matriz1 = [[(0,0),(1,0)],[(1,0),(0,0)]]
    matriz2 = [[(math.sqrt(2)/2,0),(math.sqrt(2)/2,0)],
          [(math.sqrt(2)/2,0),(-math.sqrt(2)/2,0)]]
    a = Vectores_matrices.unitaria(matriz1)
    b = Vectores_matrices.unitaria(matriz2)
    if a == True and b == True:
        r1 = Vectores_matrices.productoMatrices(matriz1,matriz2)
        resultante = Vectores_matrices.unitaria(r1)
        return resultante
    else:
        return False
    
def billar():
    #Ejercicio 4.4.2
    shot = 3
    matriz =[[(0,0),( 1/ (math.sqrt(2)),0),( 1/ (math.sqrt(2)),0),(0,0)],
             [(0, 1/ (math.sqrt(2))),(0,0),(0,0),( 1/ (math.sqrt(2)),0)],
             [( 1/ (math.sqrt(2)),0),(0,0),(0,0),(0, 1/ (math.sqrt(2)))],
             [(0,0),( 1/ (math.sqrt(2)),0),(-1/ (math.sqrt(2)),0),(0,0)]]
    vector = [(1,0),(0,0),(0,0),(0,0)]
    for i in range(shot):
        resultado = Vectores_matrices.accion(matriz,vector)
    probabilidad = (norma(resultado[3]))**2
    return probabilidad
