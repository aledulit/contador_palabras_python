#Paso 1: Solicitar al usuario que ingrese el radio del círculo que quiera calcular.

radio = float (input ("Por favor, ingrese el radio del círculo que desea calcular: "))

#Paso 2: Calcular el área del círculo utilizando la fórmula area = pi * r^2

import math
pi = math.pi

area = pi * radio **2


#Paso 3: Mostrar al usuario el área calculada

print("El área del círculo con radio", radio, "es:", area)