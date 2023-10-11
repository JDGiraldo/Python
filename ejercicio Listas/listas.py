#Importar las clases que utilizare
from nodes import node

#Creamos la clase de listas
class simpleLikenList:
    #Constructor de la clase que permite poner los parametros
    def __init__(self):
        self.first = None #Nodo Inicio o Nodo Primero
        self.last = None #Nodo Ultimo o Nodo FIn
        self.size = 0 #Contador Tamaño de la lista

    #crear un metodo para ver si la lita esta vacia
    def Empty(self):
        return self.first == None
    
    #Crear Metodo para incrementar una lista inicial 
    #def insertFist(self.data):
        #Verificar si se puso un dato valido 
