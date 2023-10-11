#Importar la clase Stack de la biblioteca lists
from lists import Queue2
from os import system


cola = Queue2()

#Insertar Elementos en la cola
cola.Enqueue("David",123)
cola.Enqueue("Ana","CE124")
cola.Enqueue("Luisa",456)


usuarioAtencion = cola.Dequeue()


while True:
    system("clear")

    print("Usuarios en Cola")
    #Mostrar los elementos de la cola
    cola.Show()
    print("*"*30)
    print("Usuario en Turno: ", usuarioAtencion)
    print("*"*30)
    print("Meno Opciones")
    print("1. Ingreasr Nuevo Usuario")
    print("2. Mostrar el siguiente Usuario en Turno")
    print("3. Salir")
    op = input("\n Ingrese la opcion deseada")  
   
    if op == "1":
        system("clear")
        nombre = input("Ingrese Nombre")
        idn = input("Ingrese Cedula")
        cola.Enqueue(nombre,idn)
    elif op == "2":
       usuarioAtencion = cola.Dequeue()
    elif op == "3":
        break


print("Usted a salido del programa")