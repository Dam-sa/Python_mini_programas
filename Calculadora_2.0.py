def sum (a,b):
    return (a+b)
def rest (a,b):
    return (a-b)
def mult (a,b):
    return (a*b)
def div(a,b):
    return (a/b)

x = 0

while x != 5 :
    print(f"--Calculadora--\n1.Suma\n2.Resta\n3.Multplicacion\n4.division\n5.Salir de la calculadora\n")
    try:
        x = int(input("Elige una opcion: "))
    except ValueError:
        print("Error, debes ingresar numero, no letras")
        continue
    if x == 5:
        print("Saliendo de la calculadora...")
        break
    
    a = int(input("Ingresa el primer numero: "))
    b =  int(input("Ingrese el segundo numero: "))
    
    match x:
        case 1:
            resultado = sum(a,b)
            print(f"La suma de {a} y {b} es {resultado}\n")
        case 2:
            resultado = rest(a,b)
            print(f"La resta de {a} y {b} es {resultado}\n")
        case 3:
            resultado = mult(a,b)
            print(f"La multiplicacion de {a} y {b} es {resultado}\n")
        case 4:
            if b == 0:
                print("No se puede realizar la division porque el divisor es cero\n")
            else:
                resultado = div(a,b)
                print(f"EL resultado de {a} y {b} es {resultado}\n")
    