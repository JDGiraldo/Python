#Importar la clase NODE desde la bilbioteca de nodes
from node import node
#Crear clase de lista enlazada
class SimplyLinkedList:
    #Crear constructor
    def __init__(self):
        self.first= None #Nodo de inicio o nodo primero
        self.last= None #Nodo final
        self.size = 0 #Tamano de la lista

    #Metodo para verificiar si la lista esta vacia o no
    def Empty(self):
        return self.first == None
    
    #Metodo para Insertar un elemento al inicio de la lista 
    def InsertFirst(self, data = None):
        #Verificar si se ingreso un dato valido
        if data == None:
            print("ERROR INGRESE UN DATO VALIDO ")
        else:
            #Asignar memoria y rellenar campo de datos
            newNode = node(data)
            #Verificar si la lista esta vacia
            if self.Empty():
                #Operacion para insertar un elemento en una lista vacia
                #Los punteros Inicio y fin apuntaran hacia el nuevo elemento
                self.first = self.last = newNode
            else:
                #Operacion para insertar un elemento al inicio de la lista
                #Paso 3 en el algoritmo
                newNode._next= self.first
                #paso 4 en el algoritmo
                self.first= newNode
            #el tamaño se actualiza
            self.size+=1
    #Metodo para insertar elemetnos al final de la lsita
    def InsertLast(self, data= None):
        #Verificar si se ingreso un dato valido
        if data == None:
            print("ERRO DATO NO VALIDO")
        else:
            #Asignar espacio de memoria
            newNode = node(data)
            #Verificar si la lista esta vacia
            if self.Empty():
                #Operacion para insertar elemento
                self.first=self.last=newNode
            else:
                #Operaciona para insertar un elemento al final de la lista
                self.last._next=newNode
                self.last=newNode
            #Actualizar el tamano de la lista
            self.size+=1
    #Operacion para insertar elemento desde cualquier parte de la lista
    def Insert(self,data=None, position=None):
        #Verificamos si se ingreso un formato valido
        if data == None:
            print("ERROR DE DATO")
        else:
            #Asignar espacio de memora en la lista
            newNode= node(data)
            #Verificar si la lista esta vacia
            if self.Empty():
                # Operación para insertar un elemento en una lista vacía
                # Los punteros inicio y fin apuntarán hacia el nuevo elemento
                self.first = self.last = newNode
                # Actualizar el tamaño de la lista
                self.size += 1
            # Verificar si no se ingresó un valor en la posición
            elif position == None:
                # Si no hay una posición, por defecto se adiciona el elemento al
                # final de la lista
                self.InsertLast(data)
            # Validar si no se encuentra la posición ingresada en la operación
            elif not self.Search(position):
                print("¡Error! No se encontró la posición ingresada en la operación, no es posible ingresar el dato.")
            # Ejecutar la operación para ingresar un elemento en cualquier
            # parte de la lista
            else:
                # Paso 3: Encontrar la posición en la lista para insertar el nodo.
                aux = self.first
                while aux:
                    if aux.data == str(position):
                        # Paso 4 del algoritmo
                        newNode._next = aux._next
                        # Paso 5 del algoritmo
                        aux._next = newNode
                        # Validar si el nuevo nodo es el nuevo último elemento
                        # elemento de la lista
                        if newNode._next == None:
                            self.last = newNode
                        # Actualizar el tamaño de la lista
                        self.size += 1
                        break
                    aux = aux._next

    # Operación para mostrar la lista
    def Show(self):
        if self.Empty():
            print("La lista está vacía.")
        else:
            aux = self.first
            while aux:
                print(aux.data,"",end="")
                aux = aux._next
            print("\n")
    
    # Operación para buscar un dato en la lista
    def Search(self, data):
        aux = self.first
        while aux:
            if str(data) == aux.data:
                return True
            aux = aux._next
        return False

    # Operacion para mostrar el tamaño de la lista
    def Size(self):
        return self.size
