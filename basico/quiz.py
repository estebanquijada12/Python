## base

puntos = 0

respuesta = input("¿De qué color es el cielo? ").lower()

if respuesta == "azul":
    print("¡Correcto!")
    puntos += 1
else:
    print("Incorrecto.")

print(f"Puntuación final: {puntos}/1")


##ejercicio 2:pon las preguntas en una lista de diccionarios y recórrela

import json

preguntas = [
    {"pregunta": "¿De qué color es el cielo?", "respuesta": "azul"},
    {"pregunta": "¿Cuánto es 2 + 2?", "respuesta": "4"},
    {"pregunta": "¿Cuál es la capital de Francia?", "respuesta": "parís"},
]
puntos = 0
for item in preguntas:
    respuesta_usuario = input(item["pregunta"] + " ").lower()
    if respuesta_usuario == item["respuesta"]:
        print("¡Correcto!")
        puntos += 1
print(f"Puntuación final: {puntos}/{len(preguntas)}")


##Ejercicio 2: Saca las preguntas a un fichero JSON.

Archivo = "preguntas.json"

with open(Archivo, "w") as f:##comentar esta parte si ya existe el fichero y no quieres sobreescribirlo
    json.dump(preguntas, f, indent=4)##creamos un fichero JSON con las preguntas y respuestas que ya teniamos en la lista de diccionarios.

with open(Archivo, "r") as f:
    preguntas_cargadas = json.load(f)
puntos = 0
for item in preguntas_cargadas:
    respuesta_usuario = input(item["pregunta"] + " ").lower()
    if respuesta_usuario == item["respuesta"]:
        print("¡Correcto!")
        puntos += 1
print(f"Puntuación final: {puntos}/{len(preguntas_cargadas)}")
