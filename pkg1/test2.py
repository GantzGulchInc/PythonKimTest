
from typing import List

from kim import Mapper, field

class AbstractBase2(object):

    def __str__(self):
        return '[ ' + self.__class__.__name__ + ': ' + str(self.__dict__) + ' ]'

    __repr__ = __str__

class TestName2(AbstractBase2):

    def __init__(self):
        id: str = ""
        name: str = ""

class TestNameMapper2(Mapper):

    __type__ = TestName2
    id = field.String()
    names = field.String()


class TestRoot2(AbstractBase2):

    def __init__(self):
        id: str = ""
        names: List[TestName2] = []

class TestRootMapper2(Mapper):

    __type__ = TestRoot2
    id = field.String()
    names = field.Collection(field.Nested(TestNameMapper2))

