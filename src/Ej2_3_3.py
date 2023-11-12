"""
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
Deberá solicitar el número hasta introducir uno correcto.
"""

Positivo = int(input("Please, insert a positive integer number: "))

if Positivo > 0: 
    cuentaAtras = [str(Positivo) for Positivo in range(Positivo, Positivo - 1)]



else:
    print("Please, insert a positive integer number.")





