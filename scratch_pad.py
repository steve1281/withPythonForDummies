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



# comparisons (chap6)

# unary operators
# ~
# -
# +

# binary operators
# +
# -
# *
# /
# % return the remainder
12 % 5
# 2

# ** exponent
3 ** 2
# 9

#// integer division
17 // 3
# 5

# relation operators
#  ==
# !=
# >
# <
# >=
# <=

# logical operators
# and
# or
# not

# bitwise operators
# & (and)
0b10101 & 0b11110
# 20
bin(20)
#'0b10100'

# ! (Or)
# ^ (exclusive Or)
# ~ ones complement
# << left shift
# >> right shift
0b1100 >> 2
#3
bin(3)
# '0b11'

#assignment
# =
# +=
# -=
# *=
# /=
# %=
# **=
# //=
x = 3
x **=2
x
#9

# membership
#In
'Hello' in 'Is there a Hello in here?'
#True
#not in

# is
# is not
x = 5
type(x) is int
#True
type(x) is str
# False
type(x) is float
# False

# creation of functions
def Hello():
     print ("This is my first python function.")

Hello()
# This is my first python function.


def AddIt(value1,value2):
    print(value1," + ",value2,' = ',(value1+value2))

AddIt(1,2)
# 1  +  2  =  3

# parameterised
AddIt(value2=6,value1=5)
# 5  +  6  =  11

# variable length arguments
def Hello4(argc,*argv):
    print('you passed ', argc, "arguments.")
    for arg in argv:
        print(arg)

#user input
name = input ("tell me your name")
print("Hello ",name)

# chapter 7
# decisions

testme = 6
if testme == 6:
    print("testme equals 6")

#testme equals 6

# note:  the indentation determines the block
if testme == 6:
     print("Yes it does")
     print("all done")

#Yes it does
#all done

# else ...

value = int(input('a value between 0 to 10'))
if (value >0) and (value <10) :
    print ('well done')
else:
    print ('not so good!')

#a value between 0 to 10>? 5
# well done

#a value between 0 to 10>? 13
#not so good!


# chaining ifs




