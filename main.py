from flask import Flask, Response
import os

app = Flask(__name__)

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

@app.route('/')
def index():
    generador = generador_numeros_positivos()
    contador = 0
    lineas_por_pantalla = 1000
    
    def generar_datos():
        nonlocal contador
        while True:
            n = next(generador)
            resultado = conjetura_de_collatz(n)
            yield f"Resultado de {n} es: {resultado}\n"
            
            contador += 1
            if contador >= lineas_por_pantalla:
                contador = 0
            if resultado != 1:
                break

    return Response(generar_datos(), content_type='text/plain;charset=utf-8')

if __name__ == '__main__':
    app.run(debug=True)
