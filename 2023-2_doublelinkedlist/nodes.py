# Crear la clase nodo
# Clase nodo con un dato y un puntero
class node:
    # Crear el constructor de la clase
    def __init__(self, datoQueVieneDelMain = None, punteroQueVieneDelMain = None):
        self.data = str(datoQueVieneDelMain)
        self._next = punteroQueVieneDelMain
    
    # Método para visualizar la información
    def __str__(self):
        return self.data

# Clase nodo con dos datos y un puntero
class node2:
    # Crear el constructor de la clase
    def __init__(self, data1 = None, data2 = None, _next = None):
        self.data1 = str(data1) # Nombre de la persona
        self.data2 = str(data2) # Número de identificación
        self._next = _next
    
    # Método para visualizar la información
    def __str__(self):
        return self.data1 + ", id: " + self.data2

# Clase nodo con un dato y dos punteros
class node3:
    # Crear el constructor de la clase
    def __init__(self, data = None, _before = None, _next = None):
        self.data = str(data)
        self._before = _before
        self._next = _next
    
    # Método para visualizar la información
    def __str__(self):
        return self.data