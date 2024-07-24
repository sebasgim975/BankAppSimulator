from model.List.List import *
from model.List.Nodes import *

class ClientLinkedList(List):
    def __init__(self):
        # Initializes an empty linked list with a head pointer set to None and size to 0
        self.head = None
        self.size = 0

    def is_empty(self):
        # Returns True if the list is empty.
        return self.head is None

    def size(self):
        # Returns the number of elements in the list
        return self.size

    def get_first(self):
        # Returns the first element of the list if it exists, raises an exception if the list is empty
        if self.head is None:
            raise Exception("Empty List")
        return self.head.get_element()

    def get_last(self):
        # Returns the last element of the list by traversing it until the end
        if self.head is None:
            raise Exception("Empty List")
        node = self.head
        while node.get_next_node() is not None:
            node = node.get_next_node()
        return node.get_element()

    def get(self, position):
        # Retrieves an element at a specific position in the list
        if position < 0 or position >= self.size:
            raise Exception("Invalid position")
        node = self.head
        for i in range(position):
            node = node.get_next_node()
        return node.get_element()

    def find(self, element):
        # Finds the position of a specific element in the list, returns -1 if not found
        node = self.head
        position = 0
        while node is not None:
            if node.get_element() == element:
                return position
            node = node.get_next_node()
            position += 1
        return -1

    def find_username(self, username):
        # Finds the position of an element with a specific username in the list
        node = self.head
        position = 0
        while node is not None:
            if node.get_element().get_name() == username:
                return position
            node = node.get_next_node()
            position += 1
        return -1

    def find_NIF(self, NIF):
        # Finds the position of an element with a specific NIF
        node = self.head
        position = 0
        while node is not None:
            if node.get_element().get_nif() == NIF:
                return position
            node = node.get_next_node()
            position += 1
        return -1

    def find_login_info(self, name, password):
        # Finds the position of an element with specific login credentials
        node = self.head
        position = 0
        while node is not None:
            if node.get_element().get_name() == name and node.get_element().get_password() == password:
                return position
            node = node.get_next_node()
            position += 1
        return -1

    def insert(self, element, position):
        # Insert an element at a specified position in the list
        if position < 0 or position > self.size:
            raise Exception("Invalid Position")  # Ensure the position is within valid bounds
        if position == 0:
            self.insert_first(element)  # Insert at the beginning if position is 0
        elif position == self.size:
            self.insert_last(element)  # Append element if position equals list size.
        else:
            node = self.head
            for i in range(position - 1):  # Navigate to the node just before the insertion point
                node = node.get_next_node()
            new_node = SingleListNode(element, node.get_next_node())  # Create a new node pointing to the next node
            node.set_next_node(new_node)  # Set the new node as the next node of the current node
            self.size += 1

    def insert_first(self, element):
        # Insert an element at the beginning of the list
        node = SingleListNode(element, self.head)  # New node points to the former first node
        self.head = node  # Update head to new node
        self.size += 1

    def insert_last(self, element):
        # Insert an element at the end of the list
        if self.head is None:
            self.insert_first(element)  # If the list is empty, insert first
        else:
            node = self.head
            while node.get_next_node() is not None:  # Navigate to the end of the list
                node = node.get_next_node()
            new_node = SingleListNode(element, None)  # Create a new node with no next node
            node.set_next_node(new_node)  # Set the new node as the next of the last node
            self.size += 1

    def remove_first(self):
        # Remove the first element of the list
        if self.head is None:
            raise Exception("Empty List")
        element = self.head.get_element()  # Retrieve the element to be removed
        self.head = self.head.get_next_node()  # Set head to the next node
        self.size -= 1
        return element

    def remove_last(self):
        # Remove the last element of the list
        if self.head is None:
            raise Exception("Empty List")
        if self.size == 1:
            return self.remove_first()  # If only one element, use remove_first
        node = self.head
        while node.get_next_node().get_next_node() is not None:
            node = node.get_next_node()  # Navigate to the second to last node
        element = node.get_next_node().get_element()  # Get the last element
        node.set_next_node(None)  # Remove the last node
        self.size -= 1
        return element

    def remove(self, position):
        # Remove an element at a specified position
        if position < 0 or position >= self.size:
            raise Exception("Invalid Position")  # Check for valid position
        if position == 0:
            return self.remove_first()  # Use remove_first if removing the first element
        if position == self.size - 1:
            return self.remove_last()  # Use remove_last if removing the last element
        node = self.head
        for i in range(position - 1):
            node = node.get_next_node()  # Navigate to the node just before the one to remove
        element = node.get_next_node().get_element()  # Get the element to be removed
        node.set_next_node(node.get_next_node().get_next_node())  # Set next to skip the removed node
        self.size -= 1
        return element

    def make_empty(self):
        # Clear all elements from the list
        self.head = None
        self.size = 0

    def iterator(self):
        # Create an iterator to traverse the list
        node = self.head
        while node is not None:
            yield node.get_element()  # Yield each element one by one
            node = node.get_next_node()
