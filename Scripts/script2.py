# Ejercicio 2 Proyecto
# Enrique Lopez Serrano
# Importamos librerias necesarias
import os
import random
import string
from datetime import datetime
from datetime import date

# Definir variables
virus = "ccucggcgggca"
virus2 = (["ccu","cgg","gca"])
num_de_grupos = 17
fecha = datetime.now().strftime('%d-%m-%Y')
hora = datetime.now().strftime('%H:%M')

# Creacion de cadena
cadena = "".join(random.choices(virus2, k=num_de_grupos))

# Informe
Codigo = input(("Introduce codigo de paciente: "))
print("Informe de virus COVID:")
print("-----------------------")
print("Fecha:" ,fecha)
print("Hora:" ,hora)
print("Codigo del Paciente:" ,Codigo)
print("Resultado:")
print("----------")
if virus in cadena:
    print("Resultado positivo: Se han encontrado restos de la variante")
    Resultado="Positivo"
else:
    print("Resultado negativo: No se han encontrado restos de la variante")
    Resultado="Negativo"

# Tupla
tupla = (fecha, hora, Codigo, Resultado)
print(tupla)
