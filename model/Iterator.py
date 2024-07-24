from abc import ABC
from model.List.Iterator import *


class Iterator(Iterator):
    def __init__(self, collection):
        # Initialize the iterator with a specific collection and set the starting index to zero.
        self._collection = collection
        self._index = 0

    def has_next(self):
        # Check if there are more elements in the collection beyond the current index.
        return self._index < len(self._collection)

    def get_next(self):
        # Return the next element in the collection if it exists, otherwise return None.
        if not self.has_next():
            return None  # If no next element, return None indicating end of collection.
        value = self._collection[self._index]  # Retrieve the current element.
        self._index += 1  # Increment the index to move to the next element.
        return value  # Return the current element.

    def rewind(self):
        # Reset the index to zero, allowing the iterator to start over from the beginning of the collection.
        self._index = 0
