# this is just a spot to keep the console commands in one place
#
# some basic commands
help()
copyright()
credits()
license()
# help has an interactive mode
# or one time
help('topics')

exec(open("/Users/steve1281/Desktop/python/withPythonForDummies/Chapter04/FirstApp.py").read())
#This is a simple Python application.
exec(open("Chapter04/FirstApp.py").read())
#This is a simple Python application.

test = 0b100
test
#4
test = 0o100
test
#64
test = 0x100
test
#256
test = 256
bin(test)
#'0b100000000'
oct(test)
#'0o400'
hex(test)
#'0x100'

type(test)
#<class 'int'>

myStr = str(1234.4)
type(myStr)
# <class 'str'>
myStr
# '1234.4'

# to bring a module (library?) into the repl, use import
import datetime

datetime.datetime.now()
#datetime.datetime(2014, 12, 4, 6, 49, 22, 572848)


datetime.datetime.now().date()
# datetime.date(2014, 12, 4)
str(datetime.datetime.now().date())
# '2014-12-04'







