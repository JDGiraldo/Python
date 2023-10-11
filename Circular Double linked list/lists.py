# Importar la clase "node" desde la biblioteca "nodes"
from nodes import node, node2, node3

# Crear la clase Lista Simplemente Enlazada
class SimplyLinkedList:
    
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
            print("¡Error! No se ingresó un dato válido, no es posible adicionar el elemento en la lista.") 
        else:
            # Asignar memoria y rellenar el campo de datos
            newNode = node(data)
            # Verificar si la lista está vacía
            if self.Empty():
                # Operación para insertar un elemento en una lista vacía
                # Los punteros inicio y fin apuntarán hacia el nuevo elemento
                self.first = self.last = newNode
            else:
                # Operación para insertar un elemento al inicio de la lista
                # Paso 3 en el algoritmo
                newNode._next = self.first
                # Paso 4 en el algoritmo
                self.first = newNode
            # El tamaño se actualiza
            self.size += 1
    
    # Método para insertar elementos al final de la lista
    def InsertLast(self, data = None):
        # Verificar si se ingresó un dato válido
        if data == None:
            print("¡Error! No se ingresó un dato válido, no es posible adicionar el elemento en la lista.") 
        else:
            # Asignar memoria y rellenar el campo de datos
            newNode = node(data)
            # Verificar si la lista está vacía
            if self.Empty():
                # Operación para insertar un elemento en una lista vacía
                # Los punteros inicio y fin apuntarán hacia el nuevo elemento
                self.first = self.last = newNode
            else:
                # Operación para insertar un elemento al final de la lista
                # Paso 3 en el algoritmo
                self.last._next = newNode
                # Paso 4 en el algoritmo
                self.last = newNode
            # Actualizar el tamaño de la lista
            self.size += 1
    
    # Operación para insertar un elemento en cualquier parte de la lista
    def Insert(self, data = None, position = None):
        # Verificar si se ingresó un dato válido
        if data == None:
            print("¡Error! No se ingresó un dato válido, no es posible adicionar el elemento en la lista.") 
        else:
            # Asignar memoria y rellenar el campo de datos
            newNode = node(data)
            # Verificar si la lista está vacía
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
            # Paso 1 ya está listo, el puntero último (self.last) almacena
            # al elemento que se desea eliminar
            # Paso 2 en el algoritmo
            aux = self.first
            while aux._next != self.last:
                aux = aux._next
            # Paso 3 en el algoritmo
            aux._next = self.last._next
            # Paso 4 en el algoritmo
            self.last = aux
            # Actualizar el tamaño de la lista
            self.size -= 1

    # Borrar cualquier elemento de la lista
    def Delete(self, data=None):
        #Validar si la lista esta vacia
        if self.Empty():
            print("Error No es posible eliminar un elemento de una lista vacia")
        #Validar si queda un solo elemento en la lista
        elif self.first ==self.last:
            self.first = self.last = None
            #Actualizar el tamaño de la lista
            self.size -=1
        #Validar si no se ingreso un dato a elimar
        elif not data:
            #Por defecto voy a eliminar el ultimo dato de la lista
            self.DeleteLast()
        #Validar si el elemento que voy a eliminar es el primero de lista
        elif str(data) == self.first.data:
            #Eliminar el primer elemento de la lista
            self.DeleteFirst()
        #Verificar si el elemento existe
        elif not self.Search(data):
            print("Error el elemento ingresado no existe en la lista, no es posible eliminarlo")
        #Operación eliminar un elemento en cualquier parte de la lista
        else:
            #Paso 1 en el algoritmo
            aux= self.first
            while aux._next.data != str(data):
                aux = aux._next
            #Paso 2 en algoritmo
            aux._next=aux._next._next
            #validar si el elemento acutal es el penultimo en la lista
            if aux._next == None:
                self.last = aux
            #Actualizar el tamaño de la lista
            self.size -= 1
    
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
        
# Crear una pila
class Stack:
    
    # Constructor de la pila
    def __init__(self):
        self.first = None # Primer elemento de la pila
        self.top = None # Cima o tope de la pila (último elemento)
        self.size = 0 # Tamaño de la pila (cantidad de elementos)
    
    # Operación para verificar si la pila está vacía
    def Empty(self):
        return self.top == None
    
    # Operación para apilar elementos
    def Push(self, data = None):
        # Verificar si se ingresó un dato válido
        if data == None:
            print("¡Error! No se ingresó un dato válido, no es posible adicionar el elemento en la lista.") 
        else:
            # Asignar memoria y rellenar el campo de datos
            newNode = node(data)
            # Verificar si la pila está vacía
            if self.Empty():
                # Operación para insertar un elemento en una pila vacía
                # Los punteros inicio y fin apuntarán hacia el nuevo elemento
                self.first = self.top = newNode
            else:
                # Operación para insertar un elemento al final de la pila (push)
                # Paso 3 en el algoritmo
                self.top._next = newNode
                # Paso 4 en el algoritmo
                self.top = newNode
            # Actualizar el tamaño de la lista
            self.size += 1
    
    # Operación para desapilar un elemento de la pila (pop)
    def Pop(self):
        # Validar si la pila está vacía
        if self.Empty():
            print("¡Error! No es posible eliminar un elemento en una lista vacía.")
        # Validar si queda un solo elemento en la pila
        elif self.first == self.top:
            data = self.top.data
            self.first = self.top = None
            # Actualizar el tamaño de la pila
            self.size -= 1
        # Operación eliminar un elemento al final de la pila (pop)
        else:
            data = self.top.data
            # Paso 1 ya está listo, el puntero último (self.top) almacena
            # al elemento que se desea eliminar
            # Paso 2 en el algoritmo
            aux = self.first
            while aux._next != self.top:
                aux = aux._next
            # Paso 3 en el algoritmo
            aux._next = self.top._next
            # Paso 4 en el algoritmo
            self.top = aux
            # Actualizar el tamaño de la lista
            self.size -= 1
        return data

    # Operación para obtener la cima o tope de la pila
    def Top(self):
        return self.top
    
    # Operacion para mostrar el tamaño de la pila
    def Size(self):
        return self.size
        
    # Operación para mostrar la pila
    def Show(self):
        aux = self.first
        while aux:
            print(aux)
            aux = aux._next


# Crear una cola
class Queue:
    
    # Constructor de la cola
    def __init__(self):
        self.front = None # Elemento frontal de la cola 
        self.rear = None # Último elemento de la cola
        self.size = 0 # Tamaño o cantidad de elementos en la cola
    
    # Operación para verificar si la cola está vacía
    def Empty(self):
        return self.front == None
    
    # Operación para insertar un elemento en la cola
    def Enqueue(self, data = None):
        # Verificar si se ingresó un dato válido
        if data == None:
            print("¡Error! No se ingresó un dato válido, no es posible adicionar el elemento en la lista.") 
        else:
            # Asignar memoria y rellenar el campo de datos
            newNode = node(data)
            # Verificar si la cola está vacía
            if self.Empty():
                # Operación para insertar un elemento en una cola vacía
                # Los punteros inicio y fin apuntarán hacia el nuevo elemento
                self.front = self.rear = newNode
            else:
                # Operación para insertar un elemento al final de la cola (enqueue)
                # Paso 3 en el algoritmo
                self.rear._next = newNode
                # Paso 4 en el algoritmo
                self.rear = newNode
            # Actualizar el tamaño de la lista
            self.size += 1
    
    # Operación para eliminar el primer elemento de la cola
    def Dequeue(self):
        # Validar si la cola está vacía
        if self.Empty():
            print("¡Error! No es posible eliminar un elemento en una cola vacía.")
        # Validar si queda un solo elemento en la cola
        elif self.front == self.rear:
            self.front = self.rear = None
            # Actualizar el tamaño de la cola
            self.size -= 1
        # Operación eliminar un elemento al inicio de la cola
        else:
            self.front = self.front._next
            # Actualizar el tamaño de la lista
            self.size -= 1
    
    # Operación para mostrar el elemento frontal de la cola
    def Front(self):
        return self.front
    
    # Operación para mostrar la cola
    def Show(self):
        aux = self.front
        while aux:
            print(aux,end=" ")
            aux = aux._next
        print("")
    
    # Operación buscar un elemento en la cola
    def Search(self, data):
        aux = self.front
        while aux:
            if aux.data == str(data):
                return True
            aux = aux._next
        return False
    
# Crear una cola con dos campos de datos en el nodo
class Queue2:
    
    # Constructor de la cola
    def __init__(self):
        self.front = None # Elemento frontal de la cola 
        self.rear = None # Último elemento de la cola
        self.size = 0 # Tamaño o cantidad de elementos en la cola
    
    # Operación para verificar si la cola está vacía
    def Empty(self):
        return self.front == None
    
    # Operación para insertar un elemento en la cola
    def Enqueue(self, data1 = None, data2 = None):
        # Verificar si se ingresó un dato válido
        if data1 == None or data2 == None:
            print("¡Error! No se ingresó un dato válido, no es posible adicionar el elemento en la lista.") 
        else:
            # Asignar memoria y rellenar el campo de datos
            newNode = node2(data1, data2)
            # Verificar si la cola está vacía
            if self.Empty():
                # Operación para insertar un elemento en una cola vacía
                # Los punteros inicio y fin apuntarán hacia el nuevo elemento
                self.front = self.rear = newNode
            else:
                # Operación para insertar un elemento al final de la cola (enqueue)
                # Paso 3 en el algoritmo
                self.rear._next = newNode
                # Paso 4 en el algoritmo
                self.rear = newNode
            # Actualizar el tamaño de la lista
            self.size += 1
    
    # Operación para eliminar el primer elemento de la cola
    def Dequeue(self):
        dataDeleted = self.front
        # Validar si la cola está vacía
        if self.Empty():
            print("¡Error! No es posible eliminar un elemento en una cola vacía.")
        # Validar si queda un solo elemento en la cola
        elif self.front == self.rear:
            self.front = self.rear = None
            # Actualizar el tamaño de la cola
            self.size -= 1
        # Operación eliminar un elemento al inicio de la cola
        else:
            self.front = self.front._next
            # Actualizar el tamaño de la lista
            self.size -= 1
        return dataDeleted
    
    # Operación para mostrar el elemento frontal de la cola
    def Front(self):
        return self.front
    
    # Operación para mostrar la cola
    def Show(self):
        aux = self.front
        while aux:
            print(aux)
            aux = aux._next
        print("")
    
    # Operación buscar un elemento en la cola
    def Search(self, data):
        aux = self.front
        while aux:
            if aux.data1 == str(data) or aux.data2 == str(data):
                return True
            aux = aux._next
        return False
    
    
# Crear la clase Lista Simplemente Enlazada
class DoubleLinkedList:
    
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
            print("¡Error! No se ingresó un dato válido, no es posible adicionar el elemento en la lista.") 
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
                # Paso nuevo en listas doblemente enlazadas
                # El puntero anterior del primer nodo apunta hacia el 
                # nuevo nodo
                self.first._before = newNode
                # Paso 5 en el algoritmo
                self.first = newNode
            # El tamaño se actualiza
            self.size += 1
    
    # Método para insertar elementos al final de la lista
    def InsertLast(self, data = None):
        # Verificar si se ingresó un dato válido
        if data == None:
            print("¡Error! No se ingresó un dato válido, no es posible adicionar el elemento en la lista.") 
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
                # Paso nuevo en listas doblemente enlazadas
                # El puntero anterior del nuevo nodo apunta hacia el
                # último elemento de la lista
                newNode._before = self.last
                # Paso 5 en el algoritmo
                self.last = newNode
            # Actualizar el tamaño de la lista
            self.size += 1
    
    # Operación para insertar un elemento en cualquier parte de la lista
    def Insert(self, data = None, position = None):
        # Verificar si se ingresó un dato válido
        if data == None:
            print("¡Error! No se ingresó un dato válido, no es posible adicionar el elemento en la lista.") 
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
                        # Paso nuevo en listas doblemente enlazadas
                        # El puntero anterior del nuevo nodo apunta hacia el
                        # elemento actual de la lista
                        newNode._before = aux
                        # Validar si el nuevo nodo es el nuevo último elemento
                        # elemento de la lista
                        if newNode._next == None:
                            self.last = newNode
                        else:
                            # Paso nuevo en listas doblemente enlazadas
                            # El puntero anterior del elemento que se encuentra
                            # después del elemento actual apunta hacia el nuevo nodo
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
            # Paso nuevo en listas doblemente enlazadas
            # El puntero anterior del primer elemento apunta a null
            self.first._before = None
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
            # Paso 1 ya está listo, el puntero último (self.last) almacena
            # al elemento que se desea eliminar
            # Paso nuevo en listas doblemente enlazadas
            # El nuevo último elemento es el penúltimo elemento
            self.last = self.last._before
            # Paso nuevo en listas doblemente enlazadas
            # El puntero siguiente del nuevo último elemento apunta a null
            self.last._next = None
            # Actualizar el tamaño de la lista
            self.size -= 1

    # Borrar cualquier elemento de la lista
    def Delete(self, data=None):
        # Validar si la lista esta vacia
        if self.Empty():
            print("¡Error! No es posible eliminar un elemento de una lista vacia")
        # Validar si queda un solo elemento en la lista
        elif self.first == self.last:
            self.first = self.last = None
            # Actualizar el tamaño de la lista
            self.size -=1
        # Validar si no se ingreso un dato a elimar
        elif not data:
            print("¡Error! Debe escribir un dato para eliminarlo de la lista")
        # Validar si el elemento que voy a eliminar es el primero de lista
        elif str(data) == self.first.data:
            #Eliminar el primer elemento de la lista
            self.DeleteFirst()
        #Verificar si el elemento existe
        elif not self.Search(data):
            print("Error el elemento ingresado no existe en la lista, no es posible eliminarlo")
        # Operación eliminar un elemento en cualquier parte de la lista
        else:
            #Paso 1 en el algoritmo
            aux = self.first
            while aux._next.data != str(data):
                aux = aux._next
            # Paso 2 en algoritmo
            aux._next = aux._next._next
            # validar si el elemento acutal es el penultimo en la lista
            if aux._next == None:
                self.last = aux
            else:
                # Paso nuevo en listas doblemente enlazadas
                # El puntero anterior del elemento que sigue al elemento actual de
                # la lista apunta hacia el elemento actual de la lista
                aux._next._before = aux
            # Actualizar el tamaño de la lista
            self.size -= 1

# Hasta aquí llegó la clase 

    # Operación para mostrar la lista de inicio a fin
    def ShowInitToEnd(self):
        if self.Empty():
            print("La lista está vacía.")
        else:
            aux = self.first
            while aux:
                print(aux.data,"",end="")
                aux = aux._next
            print("\n")
    #Operacion para mostrar la lista de fin a inciio
    def ShowEndToInit(self):
        if self.Empty():
            print("La Lista esta vacia")
        else:
            aux = self.last
            while aux:
                print(aux.data,end=" ")
                aux = aux._before
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
    
    # Crear clase de la lista circular simple
class CircularLinkedList:
    
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
            print("¡Error! No se ingresó un dato válido, no es posible adicionar el elemento en la lista.") 
        else:
            # Asignar memoria y rellenar el campo de datos
            newNode = node(data)
            # Verificar si la lista está vacía
            if self.Empty():
                # Operación para insertar un elemento en una lista vacía
                # Los punteros inicio y fin apuntarán hacia el nuevo elemento
                self.first = self.last = newNode
            else:
                # Operación para insertar un elemento al inicio de la lista
                # Paso 3 en el algoritmo
                newNode._next = self.first
                # Paso 4 en el algoritmo
                self.first = newNode
            #Actualizar el puntero siguiente del ultimo nodo para que apunte
            #hacia el primer nodo
            self.last._next = self.first
            # El tamaño se actualiza
            self.size += 1
    
    # Método para insertar elementos al final de la lista
    def InsertLast(self, data = None):
        # Verificar si se ingresó un dato válido
        if data == None:
            print("¡Error! No se ingresó un dato válido, no es posible adicionar el elemento en la lista.") 
        else:
            # Asignar memoria y rellenar el campo de datos
            newNode = node(data)
            # Verificar si la lista está vacía
            if self.Empty():
                # Operación para insertar un elemento en una lista vacía
                # Los punteros inicio y fin apuntarán hacia el nuevo elemento
                self.first = self.last = newNode
            else:
                # Operación para insertar un elemento al final de la lista
                # Paso 3 en el algoritmo
                self.last._next = newNode
                # Paso 4 en el algoritmo
                self.last = newNode
            #Actualizar el puntero siguiente del ultimo nodo para que apunte
            #hacia el primer nodo
            self.last._next = self.first
            # Actualizar el tamaño de la lista
            self.size += 1
    
    # Operación para insertar un elemento en cualquier parte de la lista
    def Insert(self, data = None, position = None):
        # Verificar si se ingresó un dato válido
        if data == None:
            print("¡Error! No se ingresó un dato válido, no es posible adicionar el elemento en la lista.") 
        else:
            # Asignar memoria y rellenar el campo de datos
            newNode = node(data)
            # Verificar si la lista está vacía
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
                        if newNode._next == self.first:
                            self.last = newNode
                            #Actualizar el puntero siguiente del ultimo nodo para que apunte
                            #hacia el primer nodo
                            self.last._next = self.first
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
        elif self.size ==1 :
            self.first = self.last = None
            # Actualizar el tamaño de la lista
            self.size -= 1
        # Operación eliminar un elemento al inicio de la lista
        else:
            self.first = self.first._next
            #Actualizar el puntero siguiente del ultimo nodo para que apunte
            #hacia el primer nodo
            self.last._next = self.first
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
            # Paso 1 ya está listo, el puntero último (self.last) almacena
            # al elemento que se desea eliminar
            # Paso 2 en el algoritmo
            aux = self.first
            while aux._next != self.last:
                aux = aux._next
            # Paso 3 en el algoritmo
            aux._next = self.last._next
            # Paso 4 en el algoritmo
            self.last = aux
            # Actualizar el tamaño de la lista
            self.size -= 1

    # Borrar cualquier elemento de la lista
    def Delete(self, data=None):
        #Validar si la lista esta vacia
        if self.Empty():
            print("Error No es posible eliminar un elemento de una lista vacia")
        #Validar si queda un solo elemento en la lista
        elif self.size ==1:
            self.first = self.last = None
            #Actualizar el tamaño de la lista
            self.size -=1
        #Validar si no se ingreso un dato a elimar
        elif not data:
            #Por defecto voy a eliminar el ultimo dato de la lista
            self.DeleteLast()
        #Validar si el elemento que voy a eliminar es el primero de lista
        elif str(data) == self.first.data:
            #Eliminar el primer elemento de la lista
            self.DeleteFirst()
        #Verificar si el elemento existe
        elif not self.Search(data):
            print("Error el elemento ingresado no existe en la lista, no es posible eliminarlo")
        #Operación eliminar un elemento en cualquier parte de la lista
        else:
            #Paso 1 en el algoritmo
            aux= self.first
            while aux._next.data != str(data):
                aux = aux._next
            #Paso 2 en algoritmo
            aux._next=aux._next._next
            #validar si el elemento acutal es el penultimo en la lista
            if aux._next == self.first:
                self.last = aux
                #Actualizar el puntero siguiente del ultimo nodo para que apunte
                #hacia el primer nodo
                self.last._next = self.first
            #Actualizar el tamaño de la lista
            self.size -= 1
    
    # Operación para mostrar la lista
    def Show(self):
        if self.Empty():
            print("La lista está vacía.")
        else:
            aux = self.first
            while aux:
                print(aux.data,"",end="")
                aux = aux._next
                #Verificar si la llista dio la vuelta
                if aux == self.first:
                    break
            print("\n")
    
    # Operación para buscar un dato en la lista
    def Search(self, data):
        aux = self.first
        while aux:
            if str(data) == aux.data:
                return True
            aux = aux._next
            #Verificar si la llista dio la vuelta
            if aux == self.first:
                return False


    # Operacion para mostrar el tamaño de la lista
    def Size(self):
        return self.size


# Crear la clase Lista Circular Doblemente  Enlazada
class CircularDoublyLinkedList:
    
    # Constructor de la clase
    def __init__(self):
        self.first = None # Nodo inicio o nodo primero
        self.last = None # Nodo fin o nodo último
        self.size = 0 # Tamaño de la lista
    
    # Método para verificar si la lista está vacía o no
    def Empty(self):
        return self.first == None
    
    #Operacion para actualizar punteros en el primer y ultimo nodo
    def UpdatePointers(self):
        self.last._next = self.first
        self.first._before = self.last
    
    # Método para insertar un elemento al inicio de la lista
    def InsertFirst(self, data = None):
        # Verificar si se ingresó un dato válido
        if data == None:
            print("¡Error! No se ingresó un dato válido, no es posible adicionar el elemento en la lista.") 
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
                # Paso 4 en EL ALGORITMO listas Circulares doblemente enlazadas
                # El puntero anterior del primer nodo apunta hacia el 
                # nuevo nodo
                self.first._before = newNode
                # Paso 5 en el algoritmo
                self.first = newNode
            #ACTUALIZAR PUNTEROS DEL PRIMER Y ULTIMO ELEMETO
            self.UpdatePointers()
            # El tamaño se actualiza
            self.size += 1
    
    # Método para insertar elementos al final de la lista
    def InsertLast(self, data = None):
        # Verificar si se ingresó un dato válido
        if data == None:
            print("¡Error! No se ingresó un dato válido, no es posible adicionar el elemento en la lista.") 
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
                # Paso 4 en listas doblemente enlazadas
                # El puntero anterior del nuevo nodo apunta hacia el
                # último elemento de la lista
                newNode._before = self.last
                # Paso 5 en el algoritmo
                self.last = newNode
            #ACTUALIZAR PUNTEROS DEL PRIMER Y ULTIMO ELEMETO
            self.UpdatePointers()
            # Actualizar el tamaño de la lista
            self.size += 1
    
    # Operación para insertar un elemento en cualquier parte de la lista
    def Insert(self, data = None, position = None):
        # Verificar si se ingresó un dato válido
        if data == None:
            print("¡Error! No se ingresó un dato válido, no es posible adicionar el elemento en la lista.") 
        else:
            # Asignar memoria y rellenar el campo de datos
            newNode = node3(data)
            # Verificar si la lista está vacía
            if self.Empty():
                # Operación para insertar un elemento en una lista vacía
                # Los punteros inicio y fin apuntarán hacia el nuevo elemento
                self.first = self.last = newNode
                #actualizamos los punteros
                self.UpdatePointers()
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
                       #PAso 5
                       # El puntero anterior del elemento que se encuentra
                        # después del elemento actual apunta hacia el nuevo nodo
                        aux._next._before = newNode 
                        #Paso 6
                        aux._next = newNode
                       #Paso 7
                        newNode._before = aux
                        #Validar si el newNode es el ultimo elemento
                        if newNode._next == self.first:
                            self.last = newNode
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
            # Paso 2 y paso 3
            self.UpdatePointers()
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
            # Paso 1 ya está listo, el puntero último (self.last) almacena
            # al elemento que se desea eliminar
            # Paso nuevo en listas doblemente enlazadas
            # El nuevo último elemento es el penúltimo elemento
            self.last = self.last._before
            # Paso nuevo en listas doblemente enlazadas
            # El puntero siguiente del nuevo último elemento apunta a null
            self.last._next = None
            # Actualizar el tamaño de la lista
            self.size -= 1

    # Borrar cualquier elemento de la lista
    def Delete(self, data=None):
        # Validar si la lista esta vacia
        if self.Empty():
            print("¡Error! No es posible eliminar un elemento de una lista vacia")
        # Validar si queda un solo elemento en la lista
        elif self.first == self.last:
            self.first = self.last = None
            # Actualizar el tamaño de la lista
            self.size -=1
        # Validar si no se ingreso un dato a elimar
        elif not data:
            print("¡Error! Debe escribir un dato para eliminarlo de la lista")
        # Validar si el elemento que voy a eliminar es el primero de lista
        elif str(data) == self.first.data:
            #Eliminar el primer elemento de la lista
            self.DeleteFirst()
        #Verificar si el elemento existe
        elif not self.Search(data):
            print("Error el elemento ingresado no existe en la lista, no es posible eliminarlo")
        # Operación eliminar un elemento en cualquier parte de la lista
        else:
            #Paso 1 en el algoritmo
            aux = self.first
            while aux._next.data != str(data):
                aux = aux._next
            # Paso 2 en algoritmo
            aux._next = aux._next._next
            # validar si el elemento acutal es el penultimo en la lista
            if aux._next == None:
                self.last = aux
            else:
                # Paso nuevo en listas doblemente enlazadas
                # El puntero anterior del elemento que sigue al elemento actual de
                # la lista apunta hacia el elemento actual de la lista
                aux._next._before = aux
            # Actualizar el tamaño de la lista
            self.size -= 1

# Hasta aquí llegó la clase 

    # Operación para mostrar la lista de inicio a fin
    def ShowInitToEnd(self):
        if self.Empty():
            print("La lista está vacía.")
        else:
            aux = self.first
            veces = 0 
            while aux:
                print(aux.data,"",end="")
                aux = aux._next
                if aux == self.first:
                    veces += 1
                    print("")
                if veces == 4:
                    break
            print("\n")
    #Operacion para mostrar la lista de fin a inciio
    def ShowEndToInit(self):
        if self.Empty():
            print("La Lista esta vacia")
        else:
            aux = self.last
            while aux:
                print(aux.data,end=" ")
                aux = aux._before
                if aux == self.last:
                    break
            print("\n")



    # Operación para buscar un dato en la lista
    def Search(self, data):
        aux = self.first
        while aux:
            if str(data) == aux.data:
                return True
            aux = aux._next

            if aux == self.first:
                return False

    # Operacion para mostrar el tamaño de la lista
    def Size(self):
        return self.size
    
    
    
    
    
    
    