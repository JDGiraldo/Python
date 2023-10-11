#Juan Diego Giraldo Gomez

#Importar la clase Stack de la biblioteca lists
from lists import Stack

#Crear una instancia (copia u objeto de la pila)
pila1 = Stack()
pila2 = Stack()
pila3 = Stack()


#Operacion Diferencias Simetricas
def DiferenciasSimetricas(pila1,pila2):
    #Recorrer la pila2 con los elementos de la pila1
    aux1 = pila1.first
    while aux1:
        coincidencia= False
        #Recorrer la pila 2 
        aux2 = pila2.first
        while aux2:
            #Verificar si los elementos coinciden
            if aux1.data == aux2.data:
                coincidencia = True
            aux2=aux2._next
        #Si el elemento de la pila 1 no esta en la pila 2 
        #Ingresarlo en la pila3
        if not coincidencia:
            pila3.Push(aux1.data)
        aux1 = aux1._next
    #Recorrer pila1 con los elementos de la pila2
    aux2 = pila2.first
    while aux2:
        #Recorrer la pila1
        aux1 = pila1.first
        coincidencia = False
        while aux1:
            #
            if aux1.data == aux2.data:
                coincidencia = True
            aux1 = aux1._next
        if not coincidencia:
            pila3.Push(aux2.data)
        aux2 = aux2._next


#Rellenar las pilas
pila1.Push(42)
pila1.Push(50)
pila1.Push(67)
pila1.Push(12)
pila1.Push(28)

pila2.Push(33)
pila2.Push(50)
pila2.Push(42)
pila2.Push(68)
pila2.Push(28)


#EJECUTAR OPERACION para llenar la pila3
DiferenciasSimetricas(pila1,pila2)

#Mostrar pilas
print("Pila 1")
pila1.Show()
print("Pila 2")
pila2.Show()
print("Pila 3")
pila3.Show()