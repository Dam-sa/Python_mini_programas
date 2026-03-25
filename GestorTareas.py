lista = []
x = 0

while x != 4:
    print("~~Gestor de tareas~~\n1.Agregar tarea\n2.Ver todas las tareas guardadas\n3.Eliminar una tarea\n4.Salir")
    x = int(input("Que deceas hacer: "))
    match x:
         
         case 1:
             tarea = str(input("Cual tareas deseas agregar: "))
             lista.append(tarea)
             print("Tarea agregada correctamente")
         case 2:
             print(lista)
         case 3:
             print(lista)
             eliminar = int(input("Elige cual borrar (contando desde 0): "))
             lista.pop(eliminar)
             print(f"Las tareas se han actulizado correctamente:{lista}")
         case 4:
             print("Saliendo...")