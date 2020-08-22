import Lab1CNYT as lab1
from tkinter import messagebox
import math

def suma_Vector(a,b):
    """
    En la funcion adicionVector ingresan dos vectores a y b que deben de ser un a lista de listas. Al final la funcion
    retornara una lista de listas correspondiente a la operacion entre vectores a+b. Ambos vectores deben de ser
    de igual dimension o no se podra realizar la operacion.
    """
    if len(a)!=len(b):
        messagebox.showerror("ERROR!","Los vectores no pueden ser operados, no son de igual dimension")
    else:
        rtaVector = [[None for fila in range(1)] for column in range(len(a))]

        fila = len(a)
        
        for i in range(fila):
            rtaVector[i][0] = lab1.suma(a[i][0],b[i][0])

        return rtaVector

def resta_Vector(a,b):
    """
    En la funcion adicionVector ingresan dos vectores a y b que deben de ser un a lista de listas. Al final la funcion
    retornara una lista de listas correspondiente a la operacion entre vectores a-b. Ambos vectores deben de ser
    de igual dimension o no se podra realizar la operacion.
    """
    if len(a)!=len(b):
        messagebox.showerror("ERROR!","Los vectores no pueden ser operados, no son de igual dimension")
    else:
        rtaVector = [[None for fila in range(1)] for column in range(len(a))]

        fila = len(a)
        
        for i in range(fila):
            rtaVector[i][0] = lab1.resta(a[i][0],b[i][0])

        return rtaVector

def inversoAditivo_Vector(a):
    """
    La funcion inversoAditivoVector recibe un vector complejo a que sera una lista de listas, y al final retornara el
    inverso aditivo del vector ingresado.
    """
    rtaVector = [[None for fila in range(1)] for column in range(len(a))]

    fila = len(a)
    
    for i in range(fila):
        rtaVector[i][0] = lab1.producto(a[i][0],[-1,0])

    return rtaVector

def productoEscalar_Vector(a,b):
    """
    La funcion multiplicacionEscalarVector recibe un escalar complejo b y un vector complejo a. Al
    final la funcion retornara el resultado de multiplicar el escalar por el vector.
    """
    fila = len(a)

    rta = [[None for column in range(len(a[0]))] for row in range(len(a))]

    for i in range(fila):
        rta[i][0] = lab1.producto(a[i][0],b)

    return rta

def suma_Matriz(a,b):
    """
    La funcion adicionMatriz recibe dos matrices de igual dimension a y b. Al final retorna
    una matriz que refleja la operacion de haber realizado la suma entre las dos matrices de
    igual dimension
    """
    fila = len(a)
    columna = len(a[0])
    
    if len(a)!=len(b) or len(a[0])!=len(b[0]):
        messagebox.showerror("ERROR!","Los matrices pueden ser operadas, no son de igual dimension")
    else:
        rtaMatriz = [[None for column in range(columna)] for row in range(fila)]

        for i in range(fila):
            for j in range(columna):
                rtaMatriz[i][j] = lab1.suma(a[i][j],b[i][j])

        return rtaMatriz

def inversoAditivo_Matriz(a):
    """
    La funcion inversoAditivoMatriz recibe una matriz a. Al final retorna el inverso aditivo
    de la matriz a.
    """
    fila = len(a)
    columna = len(a[0])
    
    for i in range(fila):
        for j in range(columna):
            a[i][j] = lab1.producto(a[i][j],[-1,0])

    return a

def productoEscalar_Matriz(a,b):
    """
    La funcion multiplicacionEscalarMatriz recibe una matriz compleja a y un escalar
    complejo b. Al final retorna el resultado de multiplicar el escalar por la matriz.
    """
    fila = len(a)
    columna = len(a[0])

    rta = [[None for column in range(columna)] for row in range(fila)]

    for i in range(fila):
        for j in range(columna):
            rta[i][j] = lab1.producto(a[i][j],b)

    return rta

def transpuesta_Matriz_Vector(a):
    """
    La funcion transpuestaMatrizVector recibe una matriz o un vector a. Al final retorna la
    transpuesta de la matriz o vector.
    """
    fila = len(a)
    columna = len(a[0])

    transpuesta = [[None for column in range(fila)] for row in range(columna)]

    for i in range(fila):
        for j in range(columna):
            transpuesta[j][i] = a[i][j]

    return transpuesta

def conjugado_Matriz_Vector(a):
    """
    La funcion conjugadoMatrizVector recibe una matriz o vector a. Al final retorna el
    conjugado de la matriz o vector ingresado.
    """
    fila = len(a)
    columna = len(a[0])

    rta = [[None for j in range(columna)] for i in range(fila)]

    if columna>1:
        for i in range(fila):
            for j in range(columna):
                rta[i][j] = lab1.conjugado(a[i][j])

    else:
        for i in range(fila):
            rta[i][0] = lab1.conjugado(a[i][0])

    return rta

def adjunta_Matriz_Vector(a):
    """
    La funcion adjuntaMatrizVector recibe un vector o matriz a. Al final retorna una matriz o
    vector que representa la adjunta de la matriz o vector.
    """
    conj = a[:]
    newConj = conjugado_Matriz_Vector(conj)
    trans = transpuesta_Matriz_Vector(newConj)

    return trans

def producto_Matriz(a,b):
    """
    La funcion productoMatriz recibe dos matrices a y b que deben de ser de tamaños compatibles. Al
    final retorna el producto (a*b) entre ambas matrices.
    """
    filaA = len(a)
    filaB = len(b)
    columnaA = len(a[0])
    columnaB = len(b[0])

    if columnaA!=filaB:
        messagebox.showerror("ERROR!","Los matrices pueden ser operadas, no son compatibles")
    else:
        rta = [[[0,0] for columna in range(columnaB)] for fila in range(filaA)]

        for i in range(filaA):
            for j in range(columnaB):
                for k in range(filaB):
                    rta[i][j] = lab1.suma(rta[i][j],lab1.producto(a[i][k],b[k][j]))

        return rta

def accion_MatrizSobreVector(a,b):
    """
    La funcion accionMatrizSobreVector recibe una matriz a y un vector b. Al final retorna
    el producto entre la matriz por el vector.
    """
    return producto_Matriz(a,b)

def productoInterno_Vector(a,b):
    """
    La funcion productoInternoVector recibe dos vectores a y b. Retornara el producto
    interno entre ambos vectores.
    """
    newVector = adjunta_Matriz_Vector(a)

    return producto_Matriz(newVector,b)

def normaVector(a):
    """
    La funcion normaVector recibe un vector a. Retorna un real que sera la norma del vector.
    """
    fila = len(a)
    columna = len(a[0])

    rta = 0

    for i in range(fila):
        for j in range(columna):
            rta += a[i][j][0]**2+a[i][j][1]**2

    return math.sqrt(rta)

def distanciaVector(a,b):
    """
    La funcion distanciaVector recibe dos vectores a y b. Retorna un real que sera la
    distancia entre ambos vectores.
    """
    resta = resta_Vector(a,b)

    norma = normaVector(resta)

    return norma

def matrizUnitaria(a):
    """
    La funcion matrizUnitaria recibe como parametro una matriz a. Retorna un booleano(True/False)
    que representara si la matriz es unitaria(True) o no lo es(False)
    """
    daga = adjunta_Matriz_Vector(a)
    operacion = producto_Matriz(a,daga)

    fila = len(a)
    columna = len(a[0])

    matrizIdentidad = [[[1,0] if x==y else [0,0] for y in range(columna)] for x in range(fila)]

    for i in range(fila):
        for j in range(columna):
            operacion[i][j] = [round(operacion[i][j][0]),round(operacion[i][j][1])]

    if operacion==matrizIdentidad:
        return True
    else:
        return False

def matrizHermitiana(a):
    """
    La funcion matrizHermitiana recibe una matriz a. Retorna un booleano(True/False) indicando
    si la matriz es hermitiana(True) o no lo es(False).
    """
    daga = adjuntaMatrizVector(a)

    if daga==a:
        return True
    else:
        return False

def productoTensorial_Matriz_Vector(a,b):
    """
    La funcion productoTensorialMatrizVector recibe dos vectores o matrices a y b, en donde a
    sera la estructura y b sera el sello. Retornara el producto tensorial entre ambos vectores o
    matrices.
    """
    filaM1,filaM2 = len(a),len(b)
    columnaM1,columnaM2 = len(a[0]),len(b[0])

    nuevaMatriz = [[[0,0] for column in range(columnaM1*columnaM2)] for row in range(filaM1*filaM2)]

    for i in range(len(nuevaMatriz)):
        for j in range(len(nuevaMatriz[0])):
            nuevaMatriz[i][j] = lab1.producto(a[i//filaM2][j//columnaM2],b[i%filaM2][j%columnaM2])


    return nuevaMatriz
