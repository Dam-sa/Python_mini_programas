x = 0
while x != 6:

    print("--Calculadora--")

    print(f"\n1.Suma\n 2.Resta\n 3.Multiplicacion\n 4.Division\n 5.Potencia\n 6.Salir")

    x = int(input("Elige una opcion:"))

    match x:

        case 1:
            a = int(input("Ingrese el Primer numero a sumar:"))
            b = int(input("Ingrese el Segundo numero a sumar:"))
            print(f"La suma de {a} y {b} es: {a+b}")
        case 2:
            a = int(input("Ingrese el Primer numero a restar:"))
            b = int(input("Ingrese el Segundo numero a restar:"))
            print(f"La resta de  {a} y {b}  es:  {a-b}")
        
        case 3:
            a = int(input("Ingrese el Primer numero a Multiplicar:"))
            b = int(input("Ingrese el Segundo numero a Multiplicar:"))
            print("La multiplicacion de ", a ,"y", b ,"es:", (a*b))

        case 4:
            a = int(input("Ingrese el Primer numero a Dividir:"))
            b = int(input("Ingrese el Segundo numero a Dividir:"))
            
            if b == 0:
                print("No se puede dividir entre 0")
            else:
                print("La division de ", a ,"y", b ,"es:", (a/b))
                
        case 5:
            a = int(input("Ingrese el Primer numero de la Potencia:"))
            b = int(input("Ingrese el Segundo numero de la Potencia:"))
            print(f"El resultado de la potencia entre ", a , " ", b, "es: ", (a**b))
            
        case _:
            print("Opcion no valida.")