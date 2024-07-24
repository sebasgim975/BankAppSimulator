from abc import ABC, abstractmethod

class Iterator(ABC):
    @abstractmethod
    def has_next(self):
            ''' Returns True if the iteration has more elements. '''
    @abstractmethod
    def get_next(self):
            ''' Returns the next element in the iteration. '''
    @abstractmethod
    def rewind(self):
            ''' Restarts the iteration. If the iteration is not empty,
             it will return the first element in the iteration.'''