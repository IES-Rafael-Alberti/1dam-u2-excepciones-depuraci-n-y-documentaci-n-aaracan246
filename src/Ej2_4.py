"""
Ahora que ya sabemos como funciona el algoritmo de burbuja, pasemos a la práctica. 
Implementación en Python y utiliza el debugger para asegurarte que funciona adecuadamente y entiendes su funcionamiento.
"""

def metodoBurbuja(array):
    n = len(array)

    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array [j+1]:
                array[j], array[j+1] = array[j+1], array[j]



if __name__ == "__main__":

    lista = [3, 2, 13, 23, 22, 357, 1, 12]

    print("Lista desordenada:", lista)

    metodoBurbuja(lista)

    print("Lista ordenada:", lista)



#Repasar esto. Añadir documentación.




