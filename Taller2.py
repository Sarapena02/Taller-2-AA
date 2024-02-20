def adivinar_numero(n):
    menor = 1
    maximo = n
    while menor <= maximo:
        numero_adivinado = (menor + maximo) // 2
        print("¿Es {} tu número?".format(numero_adivinado))
        respuesta = input("Respuesta: ").lower()
        if respuesta == "igual":
            print("¡Adiviné el número {}!".format(numero_adivinado))
            break
        elif respuesta == "mayor":
            menor = numero_adivinado + 1  # Ajustar el límite inferior
        else:
            maximo = numero_adivinado - 1  # Ajustar el límite superior

def juego_adivinar_numero():
    numero_secreto = int(input("Elige un número secreto: "))
    print("Piensa en tu número, yo intentaré adivinarlo. Recuerda que tus opciones son: mayor, menor o igual")
    adivinar_numero(numero_secreto)

# Iniciar el juego
juego_adivinar_numero()

