# Importar la clase "node" desde la biblioteca "nodes"
from nodes import node
 
# Crear la clase Lista Simplemente Enlazada
class DoubleLinkedList:
    
    # Constructor de la clase
    def __init__(self):
        self.first = None # Nodo inicio o nodo primero
        self.last = None # Nodo fin o nodo último
        self.size = 0 # Tamaño de la lista
        self.song = None #Puntero que indica la cancion en reproduccion
    
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
                print(aux.data)
                aux = aux._next
    
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
    
    #Mostrar Cancion
    def GetSong(self):
        return self.song

    #Operacion para reproducir cancion
    def Play(self, watSong = None):
        #Verificar si no hay canción Asingada
        if self.song == None:
            self.song = self.first
        
        #Verifico a que song pasar
        if watSong =="n" and self.song._next != None:
            self.song = self.song._next
        elif watSong =="b" and self.song._before != None:
            self.song = self.song._before
    
    
    
    
    