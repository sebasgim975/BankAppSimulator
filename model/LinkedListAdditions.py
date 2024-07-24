from model.List.List import *
from model.List.Nodes import *

class LinkedListAdditions(List):
    def __init__(self):
        # Initialize the linked list with head set to None and size to 0
        self.head = None
        self.size = 0

    def is_empty(self):
        # Check if the list is empty by verifying if the head is None
        return self.head is None

    def size(self):
        # Return the number of elements in the list, uses '_size' attribute
        return self.size

    def get_first(self):
        # Retrieve the first element of the list; if the list is empty, raise an Exception
        if self.head is None:
            raise Exception("Empty List")
        return self.head.get_element()

    def get_last(self):
        # Retrieve the last element of the list; if the list is empty, raise an Exception
        if self.head is None:
            raise Exception("Empty List")
        node = self.head
        # Traverse the list to find the last element
        while node.get_next_node() is not None:
            node = node.get_next_node()
        return node.get_element()

    def get(self, position):
        # Retrieves an element from a specific position in the linked list.
        if position < 0 or position >= self.size:
            raise Exception("Invalid Position")  # Check for valid index range
        node = self.head
        for i in range(position):
            node = node.get_next_node()  # Traverse to the desired position
        return node.get_element()  # Return the element at the position

    def find(self, category_element, element_data, x, y):
        # Find method to locate a node where the element matches certain criteria.
        node = self.head
        position = 0
        while node is not None:
            # Checks based on presence or absence of specific data or category elements
            if element_data is None:
                if node.get_element()[x] == category_element:
                    return position
            elif category_element is None:
                if node.get_element()[y] == element_data:
                    return position
            else:
                if node.get_element()[x] == category_element and node.get_element()[y] == element_data:
                    return position
            node = node.get_next_node()
            position += 1
        return -1  # Return -1 if no match found

    def find_name_nif(self, name):
        # Finds the position of a node based on a specified name attribute.
        node = self.head
        position = 0
        while node is not None:
            if node.get_element().get_name() == name:
                return position
            node = node.get_next_node()
            position += 1
        return -1

    def find_NIF(self, NIF):
        # Finds the position of a node by NIF.
        node = self.head
        position = 0
        while node is not None:
            if node.get_element().get_nif() == NIF:
                return position
            node = node.get_next_node()
            position += 1
        return -1

    def find_login_info(self, name, password):
        # Locates a node where both the name and password match specified values.
        node = self.head
        position = 0
        while node is not None:
            if node.get_element().get_name() == name and node.get_element().get_password() == password:
                return position
            node = node.get_next_node()
            position += 1
        return -1  # Return -1 if no matching node is found
    
    def insert(self, element, position):
        # Insert an element at a specified position, validating the position first.
        if position < 0 or position > self.size:
            raise Exception("Invalid Position")  # Ensures the position is within valid bounds
        if position == 0:
            self.insert_first(element)  # Delegate to insert_first if position is 0
        elif position == self.size:
            self.insert_last(element)  # Delegate to insert_last if position is at the end
        else:
            node = self.head
            for i in range(position - 1):  # Find the node just before the desired position
                node = node.get_next_node()
            new_node = SingleListNode(element, node.get_next_node())  # Create a new node
            node.set_next_node(new_node)  # Insert the new node into the list
            self.size += 1  # Increment the size of the list

    def insert_first(self, element):
        # Insert an element at the beginning of the list
        node = SingleListNode(element, self.head)  # Create a new node pointing to the current head
        self.head = node  # Update the head to the new node
        self.size += 1  # Increment list size

    def insert_last(self, element):
        # Insert an element at the end of the list
        if self.head is None:
            self.insert_first(element)  # If the list is empty, use insert_first
        else:
            node = self.head
            while node.get_next_node() is not None:  # Traverse to the end of the list
                node = node.get_next_node()
            new_node = SingleListNode(element, None)  # Create a new node at the end
            node.set_next_node(new_node)  # Append the new node
            self.size += 1  # Increment list size

    def remove_first(self):
        # Remove the first element of the list
        if self.head is None:
            raise Exception("Empty List")  # Cannot remove from an empty list
        element = self.head.get_element()  # Store the element to return
        self.head = self.head.get_next_node()  # Update head to the next node
        self.size -= 1  # Decrement list size
        return element  # Return the removed element

    def remove_last(self):
        # Remove the last element of the list
        if self.head is None:
            raise Exception("Empty List")  # Check if the list is empty
        if self.size == 1:
            return self.remove_first()  # If only one element, use remove_first
        node = self.head
        while node.get_next_node().get_next_node() is not None:  # Find the second-to-last node
            node = node.get_next_node()
        element = node.get_next_node().get_element()  # Store the element to return
        node.set_next_node(None)  # Remove the last node
        self.size -= 1  # Decrement list size
        return element  # Return the removed element

    def remove(self, position):
        # Remove an element from a specified position in the list
        if position < 0:
            return  # Early return if the position is negative
        if position >= self.size:
            raise Exception("Invalid Position")  # Position must be within bounds of the list size
        if position == 0:
            return self.remove_first()  # Special case for removing the first element
        if position == self.size - 1:
            return self.remove_last()  # Special case for removing the last element
        node = self.head
        for i in range(position - 1):  # Navigate to the node before the target
            node = node.get_next_node()
        element = node.get_next_node().get_element()  # Retrieve the element to remove
        node.set_next_node(node.get_next_node().get_next_node())  # Bypass the target node
        self.size -= 1  # Decrement the size of the list
        return element  # Return the removed element

    def make_empty(self):
        # Clear the list completely
        self.head = None
        self.size = 0

    def iterator(self):
        # Provide an iterator to traverse through the list
        node = self.head
        while node is not None:
            yield node.get_element()  # Yield each element in the list
            node = node.get_next_node()

    def mergeSort(self, head, order):
        # Recursively sort the linked list using merge sort
        if head.next_node == None:
            return head
        mid = self.findMid(head)  # Find the middle point
        head2 = mid.next_node  # Split the list into two halves
        mid.next_node = None
        newHead1 = self.mergeSort(head, order)  # Sort the first half
        newHead2 = self.mergeSort(head2, order)  # Sort the second half
        finalHead = self.merge(newHead1, newHead2, order)  # Merge the sorted halves
        if self.getCount(finalHead) == self.size:
            self.head = finalHead  # Update head if full list sorted
        else:
            return finalHead  # Return head if sub-list sorted

    def merge(self, head1, head2, order):
        # Merge two sorted lists into one sorted list
        merged = SingleListNode(-1, None)  # Dummy node to start the merged list
        temp = merged
        while head1 != None and head2 != None:
            if order == "ascending":  # Ascending order comparison
                if head1.element[2] < head2.element[2]:
                    temp.next_node = head1
                    head1 = head1.next_node
                else:
                    temp.next_node = head2
                    head2 = head2.next_node
            elif order == "descending":  # Descending order comparison
                if head1.element[2] > head2.element[2]:
                    temp.next_node = head1
                    head1 = head1.next_node
                else:
                    temp.next_node = head2
                    head2 = head2.next_node
            temp = temp.next_node
        while head1 != None:  # Append remaining elements from head1
            temp.next_node = head1
            head1 = head1.next_node
            temp = temp.next_node
        while head2 != None:  # Append remaining elements from head2
            temp.next_node = head2
            head2 = head2.next_node
            temp = temp.next_node
        return merged.next_node  # Return the start of the merged list, excluding dummy node

    def findMid(self, head):
        # This method is used to find the middle of the list.
        slow = head
        fast = head.next_node
        # Loop until the fast pointer reaches the end of the list or the node before the end.
        while (fast != None and fast.next_node != None):
            slow = slow.next_node
            fast = fast.next_node.next_node
        # When the loop completes, the slow pointer will be at the middle of the list.
        return slow

    def getCount(self, head):
        # This method counts the number of nodes in the list starting from the given head node.
        temp = head
        count = 0
        # Loop through the list until the end is reached.
        while (temp):
            count += 1
            temp = temp.next_node  # Move to the next node.
        return count
