"""
Escribir que solicite una contraseña, y si no coincide con la que se tiene, lance la excepción NameError con el mensaje, "Incorrect Password!!"
"""

contrasenaBuena = "HolaKePasa"

try:
    contrasena = input("Please, insert your password: ")

    if contrasena != contrasenaBuena:
        raise NameError("Incorrect Password!!")

    else:
        print("Contraseña aceptada.")

except NameError as e:
    print(e)



