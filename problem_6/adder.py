from abc import ABCMeta, abstractmethod


class Adder:
    """
    Abstract class used for abstract implementation of the method add.
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def add(self, x, y):
        pass
