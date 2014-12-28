__author__ = 'steve1281'
# book just changes the original - I would rather keep both.

import csv

class FormatData:
    def __init__(self,Name="",Age=0, Married=False):
        self.Name = Name
        self.Age = Age
        self.Married = Married

    def __str__(self):
        OutString = "'{0}', {1}, {2}".format(self.Name,self.Age,self.Married)
        return OutString

    # note: you should normally have setters/getters, error checking, etc.

    def SaveData(Filename = "",DataList = []):
        with open(Filename,"w",newline='\n') as csvfile:
            DataWriter = csv.writer(
                csvfile,
                delimiter='\n',
                quotechar=" ",
                quoting=csv.QUOTE_NONNUMERIC)
            DataWriter.writerow(DataList)
            csvfile.close()
            print("Data Saved.")

    def ReadData(Filename=""):
        with open(Filename,"r",newline='\n') as csvfile:
            DataReader = csv.reader(csvfile,delimiter='\n',quotechar=" ", quoting=csv.QUOTE_NONNUMERIC)
            Output=[]
            for Item in DataReader:
                Output.append(Item[0])

            csvfile.close()
            print("Data read!")
            return Output
