from problem_6.adder import Adder
from problem_6.exceptions import *


class ListAdder(Adder):

    def __init__(self, collection: list = None):
        self.collection: list = []
        if collection is not None and isinstance(collection, list):
            self.collection = collection
        else:
            raise BadCollectionType("Collection passed to __init__ wasn't a list.")

    # @property
    # def collection(self):
    #     return self.__collection__
    #
    # @collection.setter
    # def set_age(self, value: list):
    #     self.__collection__ = value

    def add(self, x: list, y: list):
        '''
        Adds two lists together and stores the resulting list as class attribute.
        :param x: First list
        :param y: Second list
        :return: Resulting list
        '''
        if x is not None and y is not None:
            self.collection = x + y
            return self.collection
        raise BadArgumentException("Provided argument is empty.")


class DictAdder(Adder):
    def __init__(self, collection: dict = None):
        self.collection: dict = {}
        if collection is not None and isinstance(collection, dict):
            self.collection = collection
        else:
            raise BadCollectionType("Collection passed to __init__ wasn't a list.")

    def add(self, x, y):
        '''
        Adds two dictionaries together and stores the resulting dictionary as class attribute.
        :param x: First dictionary
        :param y: Second dictionary
        :return: Resulting dictionary
        '''
        if x and y is not None:
            if isinstance(x, dict) and isinstance(y, dict):
                self.collection = x.extends(y)
                return self.collection
            else:
                raise BadArgumentException("Provided argument is not an instance of the dict.")
        else:
            raise BadArgumentException("Provided argument is empty.")
