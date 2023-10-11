# Importar la clase "node" desde la biblioteca "nodes"
from nodes import node
 
# Crear la clase Lista Simplemente Enlazada
class DoubleLinkedList:
    
    # Constructor de la clase
    def __init__(self):
        self.first = None # Nodo inicio o nodo primero
        self.last = None # Nodo fin o nodo último
        self.size = 0 # Tamaño de la lista
        self.pag = None #Puntero que indica la cancion en reproduccion
    
    # Método para verificar si la lista está vacía o no
    def Empty(self):
        return self.first == None
        
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
    def ShowInitToEnd(self):
        if self.Empty():
            print("La lista está vacía.")
        else:
            aux = self.first
            while aux:
                print(aux.data)
                aux = aux._next
                        
    #Mostrar Cancion
    def Getpag(self):
        print(self.pag) 
            
    #Operacion para navegar
    def Navg(self, navExplor = None):
        #Verificar si no hay canción Asingada
        if self.pag == None:
            self.pag = self.last
        
        #Verifico a que pag pasar
        if navExplor =="p" and self.pag._next != None:
            self.pag = self.pag._next
        elif navExplor =="a" and self.pag._before != None:
            self.pag = self.pag._before
