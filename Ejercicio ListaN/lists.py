#Traigo de los nodes la clase node
from nodes import node 

#Crear la clase Lista simplemente enlazada
class SimplyLinkedList:
    
    #Constructor de la clase permite poner los parametros
    def __init__(self):
        self.first = None #Nodo Inicio o Nodo primero
        self.last = None #Nodo Ultimo o Nodo fin
        self.size = 0 #Contador Tamaño de la lista

    #Crear un metodo para verificar si la lista esta vacia o no
    def Empty(self):
        return self.first == None
    
    #Metodo para incertar un elemento al inicio de la lista
    def InsertFirst(self, data):
        #Verificar si se ingreso un dato Valido
        if data == None:
            print("Error! Se debe ingresar un dato valido")
        else:
            #Asignar memoria y rellenar el campo de datos
            newNode = node(data)

            #verificar si la lista esta vacia
            if self.Empty():
                #OPERACION PARA INSERTAR UN ELEMNETO EN UNA LISTA VACIA
                #Los punteros Inicio Fin apuntaran hacia el nuevo elemento
                self.first =  self.last = newNode
            else:
                #Operacion para insertar un elemento al inicio de la lista
                #Paso3 en el algoritmo
                newNode._next = self.first
                #Paso 4
                self.first=newNode
            #Incrementar el tamaño
            self.size +=1

    #Metodo para insertar Elementos al final de la lsita
    def InsertLast(self, data=None):
         #Verificar si se ingreso un dato Valido
        if data == None:
            print("Error! Se debe ingresar un dato valido")
        else:
            #Asignar memoria y rellenar el campo de datos
            newNode = node(data)

            #verificar si la lista esta vacia
            if self.Empty():
                #OPERACION PARA INSERTAR UN ELEMNETO EN UNA LISTA VACIA
                #Los punteros Inicio Fin apuntaran hacia el nuevo elemento
                self.first =  self.last = newNode
            else:
                #Operacion para insertar un elemento al final de la lista
                #Paso3 en el algoritmo
                self.last._next= newNode
                #Paso 4 en el algoritmo
                self.last = newNode
            
            #Actualizzr el tamano de la lsita
            self.size +=1

        #Operacion para insertar un elemento en cualquier parte de la lista
    def Insert(self, data=None,position= None):
         #Verificar si se ingreso un dato Valido
        if data == None:
            print("Error! Se debe ingresar un dato valido")
        else:
            #Asignar memoria y rellenar el campo de datos
            newNode = node(data)

            #verificar si la lista esta vacia
        if self.Empty():
            #OPERACION PARA INSERTAR UN ELEMNETO EN UNA LISTA VACIA
            #Los punteros Inicio Fin apuntaran hacia el nuevo elemento
            self.first =  self.last = newNode
            #Verificar si no se ingreso un valor en la posicion
        elif position == None:
            #SI no hay una posicion por defecto se adicicona el elemento al final de la lista
            self.InsertLast(data)
            #Validar que no se encuentre en la posicion ingresada en la operacion
        elif not self.Search(position):
            print("No se encontro la posicion ingresada a lista")
            #Ejecutar la operacion para ingresar un elemento en cualquier parte de la lista
        else:
            #Paso 3: encontrar la posicion en la lista para insertar el nodo.
            aux = self.first
            while aux:
                if aux.data == position:  
                #Paso 4 
                    newNode._next = aux._next
                    #paso5
                    aux._next =newNode
                    #Valoidar si el nievo nodo es el ultimo 
                    #elemento d la lista
                    if newNode._next == None:
                        self.last=newNode
                    #Actualzar el tamano de la lista
                    self.size +=1
                    break
                aux = aux._next

    #Operacion para mostrar la lista
    def Show(self):
        if self.Empty():
            print("Lista vacia")
        else:
            aux = self.first
            while aux:
                print(aux.data, "",end ="")
                aux =aux._next
            print("\n")

    #Operacion para mostar el taman1o de la lista
    def Size(self):
        return self.size
