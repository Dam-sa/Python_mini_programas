import random
numero_secreto = random.randint(1,100)

intento = 0

print("Adivina un numero del 1 al 100")

while True:
    intento = int(input("Ingresa un numero: "))
    
    if intento < numero_secreto:
        print("Muy bajo")
    elif intento > numero_secreto:
        print("Muy alto")
    else:
        print("Adivinaste el numero")
        break