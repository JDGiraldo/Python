from node import node, node2, node3

class DoubleLinkedlist:
    
    # Constructor de la clase
    def __init__(self):
        self.first = None # Nodo inicio o nodo primero
        self.last = None # Nodo fin o nodo último
        self.size = 0 # Tamaño de la lista
    
    # Método para verificar si la lista está vacía o no
    def Empty(self):
        return self.first == None
    
    # Método para insertar un elemento al inicio de la lista
    def InsertFirst(self, data = None):
        # Verificar si se ingresó un dato válido
        if data == None:
            print("¡Error! No se ingresó un dato válido. no es posible adicionar el elemento en la lista.") 
        else:
            # Asignar memoria y rellenar el campo de datos
            newNode = node3(data)
            # Verificar si la lista está vacía
            if self.Empty():
                # Operación para insertar un elemento en una lista vacía
                # Los punteros inicio y fin apuntarán hacia el nuevo elemento
                self.first = self.last = newNode
            else:
                # Operación para insertar un elemento al inicio de la lista
                # Paso 3 en el algoritmo
                newNode._next = self.first
                #Paso NUEVO en listas Doblemente enlazadas
                #El puntero anterior del primer nodo apunta 
                # hacia el nuevo Nodo
                self.first._before = newNode
                # Paso 5 en el algoritmo
                self.first = newNode
            # El tamaño se actualiza
            self.size += 1
    
    # Método para insertar elementos al final de la lista
    def InsertLast(self, data = None):
        # Verificar si se ingresó un dato válido
        if data == None:
            print("¡Error! No se ingresó un dato válido. no es posible adicionar el elemento en la lista.") 
        else:
            # Asignar memoria y rellenar el campo de datos
            newNode = node3(data)
            # Verificar si la lista está vacía
            if self.Empty():
                # Operación para insertar un elemento en una lista vacía
                # Los punteros inicio y fin apuntarán hacia el nuevo elemento
                self.first = self.last = newNode
            else:
                # Operación para insertar un elemento al final de la lista
                # Paso 3 en el algoritmo
                self.last._next = newNode
                #Paso NUEVO en listas Doblemente enlazadas
                #El puntero anterior del nuevo nodo apunta 
                # hacia el ultimo elemento de la lista
                newNode._before = self.last
                # Paso 5 en el algoritmo
                self.last = newNode
            # Actualizar el tamaño de la lista
            self.size += 1
    
    # Operación para insertar un elemento en cualquier parte de la lista
    def Insert(self, data = None, position = None):
        # Verificar si se ingresó un dato válido
        if data == None:
            print("¡Error! No se ingresó un dato válido. no es posible adicionar el elemento en la lista.") 
        else:
            # Asignar memoria y rellenar el campo de datos
            newNode = node3(data)
            # Verificar si la lista está vacía
            if self.Empty():
                # Operación para insertar un elemento en una lista vacía
                # Los punteros inicio y fin apuntarán hacia el nuevo elemento
                self.first = self.last = newNode
                # Actualizar el tamaño de la lista
                self.size += 1
            # Verificar si no se ingresó un valor en la posición
            elif position == None:
                # Si no hay una posición. por defecto se adiciona el elemento al
                # final de la lista
                self.InsertLast(data)
            # Validar si no se encuentra la posición ingresada en la operación
            elif not self.Search(position):
                print("¡Error! No se encontró la posición ingresada en la operación. no es posible ingresar el dato.")
            # Ejecutar la operación para ingresar un elemento en cualquier
            # parte de la lista
            else:
                # Paso 3: Encontrar la posición en la lista para insertar el nodo.
                aux = self.first
                while aux:
                    if aux.data == str(position):
                        # Paso 4 del algoritmo
                        newNode._next = aux._next
                       #Paso5
                        #Paso NUEVO en listas Doblemente enlazadas
                        #El puntero anterior del nuevo nodo apunta 
                        # hacia el elemneto acutal en la lista
                        newNode._before = aux
                        # Validar si el nuevo nodo es el nuevo último elemento
                        # elemento de la lista
                        if newNode._next == None:
                            self.last = newNode
                        else:
                            #Paso6
                            #Paso NUEVO en listas Doblemente enlazadas
                            #EL puntero anterior del elemento que sigue al 
                            #que se encuentra del elemento actul apunta hacia 
                            #el Nuevo Nodo
                            aux._next._before = newNode
                         # Paso 7 del algoritmo
                        aux._next = newNode
                        
                        # Actualizar el tamaño de la lista
                        self.size += 1
                        break
                    aux = aux._next

    # Operación para eliminar un elemento al inicio de la lista
    def DeleteFirst(self):
        # Validar si la lista está vacía
        if self.Empty():
            print("¡Error! No es posible eliminar un elemento en una lista vacía.")
        # Validar si queda un solo elemento en la lista
        elif self.first == self.last:
            self.first = self.last = None
            # Actualizar el tamaño de la lista
            self.size -= 1
        # Operación eliminar un elemento al inicio de la lista
        else:
            self.first = self.first._next
            # Actualizar el tamaño de la lista
            self.size -= 1
    
    # Operación para eliminar el último elemento de la lista
    def DeleteLast(self):
        # Validar si la lista está vacía
        if self.Empty():
            print("¡Error! No es posible eliminar un elemento en una lista vacía.")
        # Validar si queda un solo elemento en la lista
        elif self.first == self.last:
            self.first = self.last = None
            # Actualizar el tamaño de la lista
            self.size -= 1
        # Operación eliminar un elemento al final de la lista
        else:
            # Paso 1 ya está listo. el puntero último (self.last) almacena
            # al elemento que se desea eliminar
            #EL nuevo ultimo elemento es el penmultimo elemento
            #paso2
            self.last = self.last._before
            #El puntero siguiente del nuevo ultimo elemento apunta
            #a Null
            self.last._next = None
            # Actualizar el tamaño de la lista
            self.size -= 1

    #Borrar cualquier elemento de la lista
    def Delete(self, data=None):
        #Valirdar si la lista esta vacia
        if self.Empty():
            print("Error No es posible eliminar un elemento de una lista vacia")
        #VAlidar si queda un solo elemento en la lista
        elif self.first ==self.last:
            self.first = self.last = None
            #Actualizar el tamaño de la lista
            self.size -=1
        #VAlidar si no se ingreso un dato a elimar
        elif not data:
            print("Error")
        #Validar si el elemento que voy a eliminar es el primero de lista
        elif str(data) == self.first.data:
            #Eliminar el primer elemento de la lista
            self.DeleteFirst()
        #Verificar si el elemento existe 
        elif not self.Search(data):
            print("Error el elemento ingresado no existe en la lista. no es posible eliminarlo")
        #Operacion eliminar un elemento en cualquier parte de lalista
        else:
            #Paso 1 en el algoritmo
            aux= self.first
            while aux._next.data != str(data):
                aux = aux._next
            #Paso 2 en algoritmo
            aux._next=aux._next._next
            if aux._next == None:
                self.last = aux
            else:
            #Paso nuevo en listas doblemente enlazadas
            #El puntero 
             aux._next._before = aux
            #validar si el elemento acutal es el penultimo en la lista 
            #Actualizar el tamaño de la lista
            self.size -= 1

    # Operación para mostrar la lista
    def Show(self):
        if self.Empty():
            print("La lista está vacía.")
        else:
            aux = self.first
            while aux:
                print(aux.data)
                aux = aux._next
            print("\n")
    
    # Operación para buscar un dato en la lista
    def Search(self, data):
        aux = self.first
        while aux:
            if data == aux.data:
                return True
            aux = aux._next
        return False

    # Operacion para mostrar el tamaño de la lista
    def Size(self):
        return self.size
        