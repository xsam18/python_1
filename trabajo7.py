def suma(a, b):
    return a + b
resultado = suma (3,6)
print(resultado)

def ejemplo_return():
    print('se ejecuta')
    return
print('no se ejecuta')
ejemplo_return()

def calculadora(c,d):
    suma = c + d
    resta = c - d
    return suma, resta

res_suma, res_resta = calculadora(10, 8)
print(f"suma: {res_suma}", f"resta: {res_resta}")
