__author__ = 'steve1281'

from FormattedDataV3 import FormatData

NewData = FormatData.ReadData("TestFile.csv")

for Entry in NewData:
    print(Entry)

