__author__ = 'steve1281'

class MyClass:
    def __init__(self, Name = "Sam", Age = 32):
        self.Name = Name
        self.Age = Age

    def GetName(self):
        return self.Name

    def SetName(self, Name):
        self.Name = Name

    def GetAge(self):
        return self.Age

    def SetAge(self, Age):
        self.Age = Age

    def __str__(self):
        return "{0} is aged {1}.".format(self.Name,self.Age)

