##base

import random

opciones = [
    "Sin duda.",
    "Pregúntame más tarde.",
    "La cosa no pinta bien.",
    "Ni de broma.",
]

pregunta = input("Haz una pregunta: ")
print(f"Respuesta: {random.choice(opciones)}")


##ejercicio 1: Con random.choices() darle un peso a cada respuesta para que unas salgan más que otras(como un dado cargado).
##Y logra que se pueda preguntar varias veces sin reiniciar el programa, con una palabra para salir.

opciones = [
    "Sip.",
    "Pregúntame más tarde.",
    "NONONONO.",
]
pesos = [0.25, 0.50, 0.25]

while True:
    pregunta = input("\nHaz una pregunta (o escribe 'salir'): ").strip()
    
    if pregunta.lower() == "salir":
        print("Hasta luego.")
        break 
        
    if not pregunta:
        continue

    respuesta = random.choices(opciones, weights=pesos, k=1)[0]
    print(f"Respuesta: {respuesta}")

##Ejercicio 2: Guarda cada pregunta y su respuesta en un fichero de texto con la fecha.
##Al iniciar el programa, que te enseñe las tres últimas preguntas y respuestas.


import os
from datetime import datetime

ARCHIVO = "historial_bola.txt"

opciones = [
    "Sip.",
    "Pregúntame más tarde.",
    "NONONONO.",
]
pesos = [0.25, 0.50, 0.25]

if os.path.exists(ARCHIVO):
    with open(ARCHIVO, "r") as f:
        lineas = f.readlines()
        if lineas:
            print("--- Últimas respuestas ---")
            for linea in lineas[-3:]:
                print(linea.strip())
            

while True:
    pregunta = input("Haz una pregunta (o escribe 'salir'): ").strip()

    if pregunta.lower() == "salir":
        print("Hasta luego.")
        break

    if not pregunta:
        continue

    respuesta = random.choices(opciones, weights=pesos, k=1)[0]
    print(f"Respuesta: {respuesta}\n")

    ahora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    registro = f"[{ahora}] Pregunta: '{pregunta}' | Respuesta: {respuesta}\n"

    with open(ARCHIVO, "a", encoding="utf-8") as f:
        f.write(registro)