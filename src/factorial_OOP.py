#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")
        return None
    elif num == 0: 
        return 1
    else: 
        fact = 1
        while num > 1: 
            fact *= num 
            num -= 1
        return fact 

# Verifica si se proporcionó un argumento
if len(sys.argv) < 2:
    num_input = input("No ingresó un número. Por favor, ingrese un número: ")
else:
    num_input = sys.argv[1]

# Validar entrada del usuario
try:
    num = int(num_input)
    result = factorial(num)
    if result is not None:
        print(f"Factorial {num}! es {result}")
except ValueError:
    print("Error: Debe ingresar un número entero válido.")
    sys.exit(1)


