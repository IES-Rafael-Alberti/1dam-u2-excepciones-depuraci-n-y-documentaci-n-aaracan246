"""
Escribir un programa que pida al usuario un número entero, si la entrada no es correcta, mostrará el mensaje "La entrada no es correcta" y lanzará la excepción capturada.
"""
try:
    numero = int(input("Please, insert an integer number: "))
   
except ValueError:    
        print("La entrada no es correcta.")
     









