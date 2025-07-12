import random


def adivina_el_numero(x):

    print("-----------------------------")
    print(" Bienvenido(a) al juego! ")
    print(f"Seleciona un numero entre 1 y {x} para que la computadora intente acertar....")

    limite_inferior = 1
    limite_superior = x

    respuesta = ""
    while respuesta != "c":
        #generar prediccion 
        if limite_inferior!= limite_superior:
            prediccion = random.randint(limite_inferior, limite_superior)
        else: prediccion = limite_inferior # tambien podria ser el limite superior.

        #obtener respuesta del usuario.
        respuesta = input(f"Mi prediccion es {prediccion}. Si es muy  alta, ingresa (A). Si es muy baja, ingresa (b). Si es correcta, ingresa (C): ").lower()

        if respuesta == "a":
            limite_superior = prediccion - 1
        # Si la prediccion es muy alta, la respuesta se le restara 1.
        elif respuesta == "b":
            limite_inferior = prediccion + 1

    print(f"Genial!,La computadora a acertado, tu numero es {prediccion}")


adivina_el_numero(10)
     