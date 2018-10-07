
import json
import traceback

from kim import MappingInvalid

from pkg1 import test1, test2

def executeTest1():

    try:

        with open("test1.json", 'r') as f:
            jsonData = json.load(f)

        mapper: test1.TestRootMapper1 = test1.TestRootMapper1(data = jsonData)

        root: test1.TestRoot1 = mapper.marshal()

        print("test1: ", root)

    except MappingInvalid as mi:

        print("Test1: An exception occured")
        print(mi)
        print(mi.errors)
        traceback.print_exc()

def executeTest2():

    try:

        with open("test2.json", 'r') as f:
            jsonData = json.load(f)

        mapper: test2.TestRootMapper2 = test2.TestRootMapper2(data = jsonData)

        root: test2.TestRoot2 = mapper.marshal()

        print("test1: ", root)

    except MappingInvalid as mi:

        print("Test2: An exception occured")
        print(mi)
        print(mi.errors)
        traceback.print_exc()


if (__name__ == '__main__'):


    executeTest1()

    executeTest2()

    pass

