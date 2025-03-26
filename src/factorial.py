#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
# import sys
# def factorial(num): 
#     if num < 0: 
#         print("Factorial de un número negativo no existe")
#         return 0
#     elif num == 0: 
#         return 1
        
#     else: 
#         fact = 1
#         while(num > 1): 
#             fact *= num 
#             num -= 1
#         return fact 

# if len(sys.argv) == 0:
#    nombre = input("ingrse un numero")
#    print("Debe informar un número!")
#    sys.exit()
# num=int(sys.argv[1])
# print("Factorial ",num,"! es ", factorial(num)) 


# import sys

# def factorial(num):
#     fact = 1
#     for i in range(2, num + 1):
#         fact *= i
#     return fact

# # Obtener número del argumento o solicitarlo al usuario
# if len(sys.argv) == 0:
#     num = int(sys.argv[1])
# else:
#     num = int(input("Ingrese un número para calcular el factorial: "))

# print(f"Factorial {num}! es {factorial(num)}")


import sys

def factorial(num):
    fact = 1
    for i in range(2, num + 1):
        fact *= i
    return fact

# Función para interpretar el rango de entrada
def obtener_rango(entrada):
    if entrada.startswith('-'):  # Caso "-hasta"
        desde = 1
        hasta = int(entrada[1:])
    elif entrada.endswith('-'):  # Caso "desde-"
        desde = int(entrada[:-1])
        hasta = 60
    else:  # Caso "desde-hasta"
        desde, hasta = map(int, entrada.split('-'))
    
    # Validar que el rango sea lógico
    if desde > hasta:
        print("Error: El primer número debe ser menor o igual al segundo.")
        sys.exit(1)
    
    return desde, hasta

# Obtener el rango desde-hasta
if len(sys.argv) > 1:
    try:
        desde, hasta = obtener_rango(sys.argv[1])
    except ValueError:
        print("Error: Rango inválido. Use -hasta, desde-, o desde-hasta (ej. -10, 5-, 4-8).")
        sys.exit(1)
else:
    try:
        entrada = input("Ingrese un rango (-hasta, desde-, o desde-hasta): ")
        desde, hasta = obtener_rango(entrada)
    except ValueError:
        print("Error: Entrada inválida.")
        sys.exit(1)

# Calcular y mostrar factoriales en el rango
for num in range(desde, hasta + 1):
    print(f"Factorial {num}! es {factorial(num)}")