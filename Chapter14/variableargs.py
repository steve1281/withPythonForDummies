__author__ = 'steve1281'

class MyClass:
    def PrintList1(*args):
        for Count, Item in enumerate(args):
            print("{0}. {1}".format(Count,Item))

    def PrintList2(**kwargs):
        for Name, Value in kwargs.items():
            print("{0} likes {1}".format(Name,Value))

MyClass.PrintList1("Red","Blue","Green")
MyClass.PrintList2(George="Red",Sue="Blue",Zarah="Green")

