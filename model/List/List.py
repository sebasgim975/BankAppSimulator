
from abc import ABC, abstractmethod
class List(ABC):
    @abstractmethod
    def is_empty(self):
        ''' Returns True if the collection does not contain any elements. '''
    @abstractmethod
    def size(self):
        ''' Returns the number of elements in the collection. '''
    @abstractmethod
    def get_first(self):
        ''' Returns the first element of the collection.'''
    @abstractmethod
    def get_last(self):
        ''' Returns the last element of the collection.'''
    @abstractmethod
    def get(self, position):
        ''' Returns the element at the specified position in the collection.
            Range of valid positions: 0, ..., size()-1. '''
    @abstractmethod
    def find(self, element):
        ''' Returns the position in the collection of the first occurrence of
         the specified element, or -1 if the specified element does not occur
         in the collection. '''
    @abstractmethod
    def insert_first(self, element):
        ''' Inserts the specified element at the first position in the collection. '''
    @abstractmethod
    def insert_last(self, element):
        ''' Inserts the specified element at the last position in the collection. '''
    @abstractmethod
    def insert(self, element, position):
        ''' Insert the specified element at the specified position in the collection.
             Valid range of positions: 0, ..., size().
              If the specified position is 0, the insertion corresponds to insertFirst.
             If the specified position is size(), the insertion corresponds to insertLast.'''
    @abstractmethod
    def remove_first(self):
        '''Removes and returns the element at the first position of the collection.'''
    @abstractmethod
    def remove_last(self):
        ''' Removes and returns the element at the last position of the collection. '''
    @abstractmethod
    def remove(self, position):
        ''' Removes and returns the element at the specified position in the collection.
            Range of valid positions: 0, ..., size()-1.'''
    @abstractmethod
    def make_empty(self):
        ''' Removes all elements from the collection. '''
    @abstractmethod
    def iterator(self):
        ''' Returns an iterator of the elements of the collection (in the proper sequence). '''
