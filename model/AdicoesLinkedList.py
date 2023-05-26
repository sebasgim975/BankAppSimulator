from model.List.List import *
from model.List.Nodes import *

class AdicoesLinkedList(List):
    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.head is None
    
    def size(self):
        return self.size
    
    def get_first(self):
        if self.head is None:
            raise Exception("Lista vazia")
        return self.head.get_element()

    def get_last(self):
        if self.head is None:
            raise Exception("Lista vazia")
        node = self.head
        while node.get_next_node() is not None:
            node = node.get_next_node()
        return node.get_element()

    def get(self, posicao):
        if posicao < 0 or posicao >= self.size:
            raise Exception("Posição inválida")
        node = self.head
        for i in range(posicao):
            node = node.get_next_node()
        return node.get_element()

    def find(self, elemento_categoria, elemento_data, x, y):
        node = self.head
        posicao = 0
        while node is not None:
            if elemento_data == None:
                if node.get_element()[x] != elemento_categoria:
                    return posicao
                node = node.get_next_node()
                posicao += 1
            elif elemento_categoria == None:
                if node.get_element()[y] != elemento_data:
                    return posicao
                node = node.get_next_node()
                posicao += 1
            else:
                if node.get_element()[y] != elemento_data or node.get_element()[x] != elemento_categoria:
                    return posicao
                node = node.get_next_node()
                posicao += 1
        return -1
     
    def find_name_nif(self, nome):
        node = self.head
        posicao = 0
        while node is not None:   
            if node.get_element().get_nome() == nome:
                return posicao
            node = node.get_next_node()
            posicao += 1
        return -1
    
    def find_NIF(self, NIF):
        node = self.head
        posicao = 0
        while node is not None:
            if node.get_element().get_nif() == NIF:
                return posicao
            node = node.get_next_node()
            posicao += 1
        return -1
    
    def find_login_info(self, nome, password):
        node = self.head
        posicao = 0
        while node is not None:
            if node.get_element().get_nome() == nome and node.get_element().get_password() == password:
                return posicao
            node = node.get_next_node()
            posicao += 1
        return -1
    
    def insert(self, elemento, posicao):
        if posicao < 0 or posicao > self.size:
            raise Exception("Posição inválida")
        if posicao == 0:
            self.insert_first(elemento)
        elif posicao == self.size:
            self.insert_last(elemento)
        else:
            node = self.head
            for i in range(posicao - 1):
                node = node.get_next_node()
            new_node = SingleListNode(elemento, node.get_next_node())
            node.set_next_node(new_node)
            self.size += 1

            
    def insert_first(self, elemento):
        node = SingleListNode(elemento, self.head)
        self.head = node
        self.size += 1

    def insert_last(self, elemento):
        if self.head is None:
            self.insert_first(elemento)
        else:
            node = self.head
            while node.get_next_node() is not None:
                node = node.get_next_node()
            new_node = SingleListNode(elemento, None)
            node.set_next_node(new_node)
            self.size += 1

    
    def remove_first(self):
        if self.head is None:
            raise Exception("Lista vazia")
        elemento = self.head.get_element()
        self.head = self.head.get_next_node()
        self.size -= 1
        return elemento

    def remove_last(self):
        if self.head is None:
            raise Exception("Lista vazia")
        if self.size == 1:
            return self.remove_first()
        node = self.head
        while node.get_next_node().get_next_node() is not None:
            node = node.get_next_node()
        elemento = node.get_next_node().get_element()
        node.set_next_node(None)
        self.size -= 1
        return elemento

    def remove(self, posicao):
        if posicao < 0:
            return
        if posicao >= self.size:
            raise Exception("Posição inválida")
        if posicao == 0:
            return self.remove_first()
        if posicao == self.size - 1:
            return self.remove_last()
        node = self.head
        for i in range(posicao - 1):
            node = node.get_next_node()
        elemento = node.get_next_node().get_element()
        node.set_next_node(node.get_next_node().get_next_node())
        self.size -= 1
        return elemento

    def make_empty(self):
        self.head = None
        self.size = 0

    def iterator(self):
        node = self.head
        while node is not None:
            yield node.get_element()
            node = node.get_next_node()

    def mergeSort(self, head, order):
        if (head.next_node == None):
            return head
        
        mid = self.findMid(head)
        head2 = mid.next_node
        mid.next_node = None
        newHead1 = self.mergeSort(head, order)
        newHead2 = self.mergeSort(head2, order)
        finalHead = self.merge(newHead1, newHead2, order)
        if self.getCount(finalHead) == self.size:
            self.head=finalHead
        else:
            return finalHead
 
    def merge(self, head1,head2, order):
        merged = SingleListNode(-1, None)  
        temp = merged

        while (head1 != None and head2 != None):
            if order == "ascendente":
                if (head1.element[2] < head2.element[2]):
                    temp.next_node = head1
                    head1 = head1.next_node
                else:
                    temp.next_node = head2
                    head2 = head2.next_node
                temp = temp.next_node

            if order == "descendente":
                if (head1.element[2] > head2.element[2]):
                    temp.next_node = head1
                    head1 = head1.next_node
                else:
                    temp.next_node = head2
                    head2 = head2.next_node
                temp = temp.next_node
        
        while (head1 != None):
            temp.next_node = head1
            head1 = head1.next_node
            temp = temp.next_node
        
        while (head2 != None):
            temp.next_node = head2
            head2 = head2.next_node
            temp = temp.next_node
        
        return merged.next_node
 
    def findMid(self, head):
        slow = head
        fast = head.next_node
        while (fast != None and fast.next_node != None):
            slow = slow.next_node
            fast = fast.next_node.next_node
        return slow
    
    def getCount(self, head):
        temp = head  
        count = 0  
 
        while (temp):
            count += 1
            temp = temp.next_node
        return count
