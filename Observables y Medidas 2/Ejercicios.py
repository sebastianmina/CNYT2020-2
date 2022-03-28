import numpy as np
from Vectores_matrices import *

""" Punto 4.3.1"""
def posiblesProbabilidad(posicion, index):
    estados = [[(0,1),(1,0)],[(0,-1),(1,0)],[(1,0),(1,0)],[(-1,0),(1,0)],[(0,0),(1,0)],[(1,0),(0,0)]]
    resultado = []
    for i in range((index*2)-2,index*2):
        if probabilidad(posicion,estados[i])!= 0.0:
            resultado = resultado + estados[i]
    return resultado



""" Punto 4.4.1"""
def verificarUnitarias():
    U1 = [[(0,0),(1,0)],[(1,0),(0,0)]]
    U2 = [[((2**(1/2))/2,0),((2**(1/2))/2,0)],[((2**(1/2))/2,0),(-(2**(1/2))/2,0)]]
    if Uni(U1) and Uni(U2):
        resultado = producto_matrices_reales(U1,U2)
        return Uni(resultado)

""" Punto 4.4.2 """
def ExperimentoCanicas(vectorEstado,canicas,nclicks):
    for i in range(nclicks):
        vectorEstado = vectormatrizReal(vectorEstado,canicas)
    return vectorEstado
