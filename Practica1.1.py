# Importar las bibliotecas necesarias
import random  # Biblioteca para generar números aleatorios
import math  # Biblioteca para operaciones matemáticas
import timeit  # Biblioteca para medir tiempos de ejecución

# Crear una lista de tamaño n con números aleatorios entre 0 y 10
n = 10000
A = []
for i in range(n):
    A.append(random.randint(0, 10))

# Crear copias de la lista A
A1 = A[:]
A2 = A[:]
A3 = A[:]
n = len(A)

# Definición del algoritmo Bubble Sort
def BubbleSort(A1, n):
    # Recorre la lista n-1 veces
    for i in range(n - 1):
        # Recorre la lista desde el principio hasta n-i-1
        for j in range(0, n - i - 1):
            # Compara elementos adyacentes y los intercambia si están en el orden incorrecto
            if A1[j] > A1[j + 1]:
                tmp = A1[j]
                A1[j] = A1[j + 1]
                A1[j + 1] = tmp

# Ejecutar Bubble Sort y medir su tiempo de ejecución usando timeit
BubbleSort(A1, n)
tiempo1 = timeit.timeit(lambda: BubbleSort(A1, n), number=1)
print("\nTiempo de ejecucion Bubble Sort: {:.10f}".format(tiempo1))

# Definición del algoritmo Bubble Sort Optimizado
def BubbleSortOp(A2, n):
    flag = 1
    x = 0
    # Ejecuta hasta que no se realicen intercambios
    while (x < n-1) and (flag == 1):
        flag = 0
        # Recorre la lista desde el principio hasta n-x-1
        for j in range (n-x-1):
            # Compara elementos adyacentes y los intercambia si están en el orden incorrecto
            if (A2[j] > A2[j+1]):
                flag = 1
                tmp = A2[j]
                A2[j] = A2[j+1]
                A2[j+1] = tmp
        x = x + 1

# Ejecutar Bubble Sort Optimizado y medir su tiempo de ejecución usando timeit
BubbleSortOp(A2, n)
tiempo2 = timeit.timeit(lambda: BubbleSortOp(A2, n), number=1)
print("\nTiempo de ejecucion Bubble Sort Optimizado: {:.10f}".format(tiempo2))

# Definición de las funciones auxiliares para el Merge Sort

# Función que crea una sublista
def CrearSub(A3, izq, der):
    return A3[izq : der + 1]

# Función que combina dos sublistas ordenadas en una lista ordenada
def Merge(A3, p , q, r):
    izq = CrearSub(A3,p,q)
    der = CrearSub(A3,q+1,r)
    i = 0
    j = 0
    for k in range (p, r+1):
        # Compara elementos de las sublistas y los coloca en orden en la lista original
        if (j >=len(der)) or (i < len(izq) and izq[i] < der[j]):
            A3[k] = izq[i]
            i = i + 1
        else:
            A3[k] = der[j]
            j = j + 1

# Definición del algoritmo Merge Sort
def MergeSort(A3,p,r):
    if r - p > 0:
        q = math.floor((p+r)/2)
        # Aplica MergeSort recursivamente a las mitades izquierda y derecha
        MergeSort(A3,p,q)
        MergeSort(A3,q+1,r)
        # Combina las mitades ordenadas
        Merge(A3,p,q,r)

# Ejecutar Merge Sort y medir su tiempo de ejecución usando timeit
p = 0
r = len(A3)-1
MergeSort(A3, p, r)
tiempo3 = timeit.timeit(lambda: MergeSort(A3, p, r), number=1)
print("\nTiempo de ejecucion Merge Sort: {:.10f}".format(tiempo3))
