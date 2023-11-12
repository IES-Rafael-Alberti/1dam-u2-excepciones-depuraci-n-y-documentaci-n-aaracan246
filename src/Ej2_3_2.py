"""
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
"""
Positivo = int(input("Please, insert a positive integer number: "))

if Positivo > 0:
    impares = [str(Positivo) for Positivo in range (1, Positivo + 1, 2)]
    
    resultado = ", ".join(impares)
    
    print(f"Odd numbers from 1 to {Positivo} are: {resultado}.")

else:
    print("Please, insert a positive integer number.")



