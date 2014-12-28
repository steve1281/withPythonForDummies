__author__ = 'steve1281'

from FormattedDataV3 import FormatData
import os.path

if not os.path.isfile("Testfile.csv"):
    print("Please run the CreateFile.py example. (the file 'Testfile.csv' isn't there, see code in scratch_pad)")
    quit()

NewData = FormatData.ReadData("Testfile.csv")
for Entry in NewData:
    print(Entry)

print("\r\nAdding a record for Harry")
NewRecord = "'Harry', 23, False"
NewData.append(NewRecord)
for Entry in NewData:
    print(Entry)

print("\r\nRemoving Doug's record.")
Location = NewData.index("'Doug', 52, True")
Record = NewData[Location]

NewData.remove(Record)
for Entry in NewData:
    print(Entry)

print("\r\nModifying Sally's record")
Location = NewData.index("'Sally', 47, False")
Record = NewData[Location]
Split = Record.split(",")
NewRecord = FormatData(Split[0].replace("'",""),int(Split[1]),bool(Split[2]))
NewRecord.Married = True
NewRecord.Age = 48
NewData.append(NewRecord.__str__())
NewData.remove(Record)
for Entry in NewData:
    print(Entry)

FormatData.SaveData("ChangeFile.csv",NewData)

