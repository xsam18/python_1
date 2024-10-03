def imprimir_numeros(texto1, texto2):
    contador = 0
    for numero in range(1, 101):
        if numero % 3 == 0 and numero % 5 == 0:
            print(texto1 + texto2)  # Si es múltiplo de 3 y 5
        elif numero % 3 == 0:
            print(texto1)  # Si es múltiplo de 3
        elif numero % 5 == 0:
            print(texto2)  # Si es múltiplo de 5
        else:
            print(numero)  # Si no es múltiplo de 3 o 5
            contador += 1  # Contar números impresos

    return contador  # Retornar la cantidad de números impresos