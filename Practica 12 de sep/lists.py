#Importar la clase node y la clase node2 del node
from node import node, node2

#Crear la clase de listas enlazadas
class simpleLinkedList:
    def __init__(self):
        self.first = None#Nodo inicio o nodo primero
        self.last = None#Nodo fin o nodo ultimo
        self.size = 0#Tamaño de la lista

    #Metodo para verificar si la lista esta vacia
    def Empty(self):
        return self.first == None
    
    #Metodo para insertar un elemennto al inicio lista
    def InsertFirst(self,data = None):
        #Verificar si se ingreso un dato valido
        if data == None:
            print("Error! No ingresaste un dato valido")
        else:
            #Asignar memoria y rellenar el campo de datos
            newNode = node(data)
            #Verificar si la lista esta vacia
            if self.Empty():
                #Operacion para insertar un elemento a una lita vacia
                #Los punteros inicio y fin apuntan a un mismo elemento
                self.first = self.last = newNode
            else:
                #Operacion para insertar elemento al principio de la lista
                #paso 3 en el algoritmo
                newNode._next = self.first
                #paso 4
                self.first= newNode
            #incrementar el tamana
            self.size +=1
    #Crear metodo apra insertar elemento al final de a lista
    def InsertLast(self, data = None):
        #Verificar si se ingreso un dato valido
        if data == None:
            print("Error el elemento no es valido")
        else:
            #Asignar memoria y rellenar el campo de datos
            newNode = node(data)
            #Verificar si la lista esta vacia
            if self.Empty():
                #Operacion para insertar un elemento a lista vacia
                #Los punteros Inicio y fin apunta al nuevo elenento
                self.first = self.last = newNode
            else:
                #Operacion para insertar un elemento al final de lista 
                #paso3
                self.last._next = newNode
                #paso4
                self.last = newNode
            #Actuzaliar el tamano de la lista
            self.size +=1

    #Operacion para insertar un elemento en cualquier parte de la lista
    def Insert(self,data= None, position= None):
        #Verificar si se ingerso un dato valido
        if data == None:
            print("Error dato no valido")
        else:
            #Asignar un espacio de memoria y rellenar campo
            newNode = node(data)
            #Verificar si la lista esta vacia
            if self.Empty():
                #Operacion para ingresar un elemento a una lista vacia
                self.first = self.last = newNode
                #Actualizar el tamaño de la lsita
                self.size +=1
            elif position == None:
                #Si hay una posicion. por defecto se adiciona el elemnto al final de la lista 
                self.InsertLast(data)
            #validar si no se encuentra la posicion ingresada en la operacion 
            elif not self.Search(position):
                print("Error No se encontro la posicion ingresada")
                #Ejecutar la operacion para ingresar un elemento en cualqueir parte de lista
            else:
                #Paso 3: Encontrar la posicion en la lista para insertar 
                aux= self.first
                while aux:
                    if aux.data == str(position):
                        #paso4
                        newNode._next = aux._next
                        #Paso 5
                        aux._next = newNode
                        #Validar si el nuevo nodo es el nuevo ultimo elemento 
                        if newNode._next == None:
                            self.last = newNode
                        #Actualizar el tamano de la lista
                        self.size +=1
                        break
                    aux = aux._next



    #Operacion  para mostrar lista
    def Show(self):
        if self.Empty():
            print("La lista esta vacia")
        else:
            aux = self.first
            while aux:
                print(aux.data, " ", end=" ")
                aux = aux._next
                print("\n")

    #Operacion para buscar dato
    def Search(self, data):
        aux= self. first
        while aux:
            if str(data) == aux.data:
                return True
            aux = aux._next
        return False

    #Operacion para mostrar
    def Size (self):
        return self.size