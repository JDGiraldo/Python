#Importar la clase Stack de la biblioteca lists
from lists import Stack
from os import system

#Crear una instancia (copia u objeto de la pila)
pilaDeshacer = Stack()
pilaRehacer = Stack()

#Guardar acciones de la pila
pilaDeshacer.Push("Establecer margenes")
pilaDeshacer.Push("Escribir un titulo")
pilaDeshacer.Push("Poner Negrilla al titulo")

while True:
    #Limpiar Pantalla
    system("clear")
    print("Acciones en la pila: ")
    #Mostrar Pila
    pilaDeshacer.Show()
    print("\nMenu de Opciones:")
    print("1.Adiccionar accion den la pila")
    print("2.Deshacer(ctr+Z).")
    print("3.Reshacer(ctr+Y).")
    print("4.Mostrar Pila Rehcer.")
    print("5.Salir.")
    op= int(input("Ingrese la opcion deseada"))

    if op == 1:
        action = input("Ingrese la accion realizada: ")
        pilaDeshacer.Push(action)
    elif op == 2:
        pilaRehacer.Push(pilaDeshacer.Pop())
        #print("Ha decidido desahacer la siguiente accion: ".pilaDeshacer.Pop())
        #v= input("Presione cualquier tecla para continuar...")
    elif op == 3:
        pilaDeshacer.push(pilaRehacer.Pop())
    elif op == 4:
        print("Acciones pilas rehacer")
        pilaRehacer.Show()
        v= input("Presione cualquier tecla para continuar...")
    elif op == 5:
        break
    else:
        print("Error! a ingresado una opcion incorrecta")
        v= input("Presione cualquier tecla para continuar...")
print("Usted a salido del programa")
