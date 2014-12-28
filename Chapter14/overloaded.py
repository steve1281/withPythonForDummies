__author__ = 'steve1281'
class MyClass:
    def __init__(self,*args):
        self.Input = args

    def __add__(self, Other):
        Output = MyClass()
        Output.Input = self.Input + Other.Input
        return Output

    def __str__(self):
        Output = ""
        for Item in self.Input:
            Output += Item
            Output += " "
        return Output

Value1 = MyClass("Red","Green","Blue")
Value2 = MyClass("Yellow","Purple","Cyan")
Value3 = Value1 + Value2

print("{0} + {1} = {2}".format(Value1,Value2,Value3))
