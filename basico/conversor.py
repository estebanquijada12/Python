## Base

millas = float(input("Introduce la distancia en millas: "))
kilometros = millas * 1.60934

print(f"{millas} millas son {round(kilometros, 2)} kilómetros.")


##ejercicio 1: si se añaden millas, kilos, grados y pulgadas,
## tendrás un if / elif interminable. Sustitúyelo por un diccionario que asocie cada conversión. 

metricas = {
    "millas-kilometros": 1.60934,
    "kilos-libras": 2.20462,
    "grados-fahrenheit": lambda x : (x * 1.8) + 32,##como no es solo un factor de multiplicación, sino que hay que sumarle 32, lo hacemos con una función lambda.
    "pulgadas-centimetros": 2.54
}


##ejercicio 2: la moneda cambian cada día, así que un número fijo en el código no sirve.
# usa una API gratuita con requests y obten la cotización del día.

import requests

metricas["USD-pesos"] = requests.get("https://cl.dolarapi.com/v1/cotizaciones/usd").json()["compra"]
