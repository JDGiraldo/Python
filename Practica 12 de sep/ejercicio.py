class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)

def comparar_y_crear_pila(pila1, pila2):
    resultado = Stack()
    temp = Stack()

    while not pila1.is_empty() and not pila2.is_empty():
        elemento1 = pila1.pop()
        elemento2 = pila2.pop()

        if elemento1 == elemento2:
            resultado.push(elemento1)
        else:
            temp.push(elemento1)
            temp.push(elemento2)

    # Agregar elementos restantes de ambas pilas a la pila resultado
    while not pila1.is_empty():
        temp.push(pila1.pop())
    while not pila2.is_empty():
        temp.push(pila2.pop())

    # Invertir la pila temporal para que los elementos queden en el orden correcto
    while not temp.is_empty():
        resultado.push(temp.pop())

    return resultado

# Ejemplo de uso
pila1 = Stack()
pila1.push(1)
pila1.push(2)
pila1.push(3)
pila1.push(4)
pila1.push(5)

pila2 = Stack()
pila2.push(3)
pila2.push(4)
pila2.push(5)
pila2.push(6)
pila2.push(7)

resultado_pila = comparar_y_crear_pila(pila1, pila2)

# Mostrar la pila resultante
print("Elementos en la pila resultante:")
while not resultado_pila.is_empty():
    print(resultado_pila.pop())
