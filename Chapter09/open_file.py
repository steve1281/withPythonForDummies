__author__ = 'steve1281'

import sys

try:
    file = open('myfile.txt')
except IOError as e:
    print("Error Number: {0}\r\n".format(e.errno) +
          "Error Text: {0}".format(e.strerror))

else:
    print("File opened as expected.")
    file.close()

