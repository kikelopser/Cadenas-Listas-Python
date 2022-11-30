# Ejercicio 1 Proyecto
# Enrique Lopez Serrano
# Importar y definir la fecha y hora.
from datetime import datetime
from datetime import date
import os
import sys

# Definir variables de fecha y hora.
fecha = datetime.now().strftime('%d-%m-%Y')
hora = datetime.now().strftime('%H:%M')

# Bloque principal
temperaturas = []
while True:
    temperatura = int(input("Introduce la temperatura: "))
    if temperatura != 100:
        temperaturas.append(temperatura)
    if temperatura == 100:
        break;

# Bucle
print("Informe de temperaturas del Parque Natural de Doñana: ")
print("-----------------------------------------------------")
print("Fecha:" ,fecha)
print("Hora:" ,hora)
print("Numero de muestras: %d" % len(temperaturas))
print("Temperaturas tomadas:" ,temperaturas)
print("Temperatura maxima:" ,max(temperaturas))
print("Temperatura minima:" ,min(temperaturas))
print("Temperatura media:" ,round(sum(temperaturas)/len(temperaturas),2))
temp_tupla = (fecha,hora,temperaturas)
lista = list(temp_tupla)
file = open("temperaturasELS.txt", "a")
file.write('temperaturas = %s' % lista + '\n')
file.close()
