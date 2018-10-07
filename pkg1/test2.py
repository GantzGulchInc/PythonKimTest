
from typing import List

from kim import Mapper, field

class AbstractBase2(object):

    def __str__(self):
        return '[ ' + self.__class__.__name__ + ': ' + str(self.__dict__) + ' ]'

    __repr__ = __str__

class TestName2(AbstractBase2):

    def __init__(self):
        self.id: str = ""
        self.name: str = ""

class TestNameMapper2(Mapper):

    __type__ = TestName2
    id = field.String()
    name = field.String()


class TestRoot2(AbstractBase2):

    def __init__(self):
        self.id: str = ""
        self.names: List[TestName2] = []

class TestRootMapper2(Mapper):

    __type__ = TestRoot2
    id = field.String()
    names = field.Collection(field.Nested(TestNameMapper2, allow_create = True, allow_updates_in_place = True, allow_partial_updates = True))