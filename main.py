import os

def conjetura_de_collatz(n):
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    return n  

def generador_numeros_positivos():
    numero = 1
    while True:
        yield numero
        numero += 1

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

generador = generador_numeros_positivos()
contador = 0
lineas_por_pantalla = 1000  # Configura el número de líneas a mostrar antes de limpiar la pantalla

while True:
    n = next(generador)
    resultado = conjetura_de_collatz(n)
    print(f"Resultado de {n} es: {resultado}")

    contador += 1
    if contador >= lineas_por_pantalla:
        limpiar_pantalla()
        contador = 0

    if resultado != 1:
        break
