# Crear la clase nodo
# Clase nodo con un dato y un puntero

# Clase nodo con un dato y dos punteros
class node:
    # Crear el constructor de la clase
    def __init__(self, data = None, _before = None, _next = None):
        self.data = str(data)
        self._before = _before
        self._next = _next
    
    # Método para visualizar la información
    def __str__(self):
        return self.data