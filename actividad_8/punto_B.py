def adivinar_numero():
    limite_inferior = 1
    limite_superior = 1000
    contador = 0

    while contador < 10:
        medio = (limite_inferior + limite_superior) // 2
        print(f"¿Es {medio}?")
        respuesta = input("Responde con 'L', 'C' o 'B': ")

        if respuesta == "B":
            print(f"Número adivinado en {contador + 1} preguntas.")
            return
        elif respuesta == "L":
            limite_inferior = medio + 1
        elif respuesta == "C":
            limite_superior = medio - 1
        else:
            print("Respuesta inválida.")
            return

        contador += 1

    print("No se pudo adivinar el número.")

# Ejemplo de uso
adivinar_numero()
