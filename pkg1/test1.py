
from typing import List

from kim import Mapper, field

class AbstractBase1(object):

    def __str__(self):
        return '[ ' + self.__class__.__name__ + ': ' + str(self.__dict__) + ' ]'

    __repr__ = __str__

class TestRoot1(AbstractBase1):

    def __init__(self):
        self.id: str = ""
        self.names: List[str] = []

class TestRootMapper1(Mapper):

    __type__ = TestRoot1
    id = field.String()
    names = field.Collection(field.String())

