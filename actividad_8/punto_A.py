def buscar_elemento(array, n, b):
    i = 0
    j = n - 1

    while i <= j:
        k = (i + j) // 2  # Índice medio
        if array[k] == b:
            return k  # Elemento encontrado
        elif array[k] < b:
            i = k + 1  # Ajustar el extremo inferior
        else:
            j = k - 1  # Ajustar el extremo superior
            
    return -1  # Elemento no encontrado

# Ejemplo de uso
n = int(input("Ingrese el tamaño del array: "))
array = list(map(int, input("Ingrese los elementos del array ordenado: ").split()))
b = int(input("Ingrese el elemento a buscar: "))
posicion = buscar_elemento(array, n, b)

if posicion != -1:
    print(f"Elemento encontrado en la posición: {posicion}")
else:
    print("No se encontró el elemento")
