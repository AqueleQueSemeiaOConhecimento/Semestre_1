class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
            
        last_node.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Exemplo de uso


def lista_ligada(*args):
    
    linked_list = LinkedList()
    
    for arg in args:
        linked_list.append(arg)
    
    linked_list.display()
    

valor = []

print('LISTA LIGADA')

valor1 = input('Valor 1: ')
valor2 = input('Valor 2: ')
valor3 = input('Valor 3: ')

lista_ligada(valor1, valor2, valor3)

input('Digite Enter para encerrar')