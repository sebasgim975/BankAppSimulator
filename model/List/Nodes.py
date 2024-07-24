class SingleListNode:
    def __init__(self, element, next_node):
        # Initialize a node with an element and a reference to the next node in the list.
        self.element = element
        self.next_node = next_node

    def get_element(self):
        # Return the element stored in this node.
        return self.element

    def get_next_node(self):
        # Return the reference to the next node in the list.
        return self.next_node

    def set_element(self, element):
        # Set or update the element stored in this node.
        self.element = element

    def set_next_node(self, next_node):
        # Set or update the reference to the next node in the list.
        self.next_node = next_node


class DoubleListNode(SingleListNode):
    def __init__(self, element, next_node, previous_node):
        # Initialize as a SingleListNode and add a reference to the previous node.
        super().__init__(element, next_node)
        self.previous_node = previous_node

    def get_previous_node(self):
        # Return the reference to the previous node in the list.
        return self.previous_node

    def set_previous_node(self, previous_node):
        # Set or update the reference to the previous node in the list.
        self.previous_node = previous_node
