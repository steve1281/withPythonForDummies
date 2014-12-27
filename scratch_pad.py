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
# see breakfest_menu.py for an example

# chapter 08

# example of for loop
letternum = 1
for letter in 'howdy':
     print ('letter ',letternum, ' is ', letter)
     letternum += 1

#letter  1  is  h
#letter  2  is  o
#letter  3  is  w
#letter  4  is  d
#letter  5  is  y

# for loop with break

value = input("type less than 6 characters: ")
# type less than 6 characters: >? alphabeta
letternum =1

for letter in value:
     print("letter: ", letternum, " is ", letter)
     letternum+=1
     if letternum > 6:
         print('The string is too long!')
         break

#letter:  1  is  a
#letter:  2  is  l
#letter:  3  is  p
#letter:  4  is  h
#letter:  5  is  a
#letter:  6  is  b
#The string is too long!


# for loop with a continue
letternum =1
for letter in 'Howdy!':
     if letter == 'w':
         continue
         print ('envountered w, not processed')
     print('letter ', letternum, " is ", letter)
     letternum += 1

#letter  1  is  H
#letter  2  is  o
#letter  3  is  d
#letter  4  is  y
#letter  5  is  !

## note that print ( encountered ... ) was not processed.

# the while statement
# (prints out the 10 times table)

x = 1
y = 1
print ('{:>4}'.format(' '), end= ' ')
for x in range(1,11):
    print ('{:>4}'.format(x), end= ' ')

print()

for x in range(1,11):
    print ('{:>4}'.format(x), end= ' ')
    while y <= 10:
        print ('{:>4}'.format(x * y), end= ' ')
        y+=1
    print()
    y=1

  #      1    2    3    4    5    6    7    8    9   10
  # 1    1    2    3    4    5    6    7    8    9   10
  # 2    2    4    6    8   10   12   14   16   18   20
  # 3    3    6    9   12   15   18   21   24   27   30
  # 4    4    8   12   16   20   24   28   32   36   40
  # 5    5   10   15   20   25   30   35   40   45   50
  # 6    6   12   18   24   30   36   42   48   54   60
  # 7    7   14   21   28   35   42   49   56   63   70
  # 8    8   16   24   32   40   48   56   64   72   80
  # 9    9   18   27   36   45   54   63   72   81   90
  #10   10   20   30   40   50   60   70   80   90  100


#chapter 9 dealing with errors

# syntactical - typo
# semantic    - code is correct, but executes at wrong time. (e.g. fence post error)
# logical     - code is wrong. The algorithm is incorrect.

# types of exceptions
#  base classes
#  concrete exceptions - e.g. running out of memory
#  OS exceptions - e.g. trying to open a file that is not there
#  warnings - i.e. trying to use a class in an unintended way


# examples of exception handling...

try:
    value = int(input("type a number between 1 and 10: "))

except ValueError:
    print("you must type a number between 1 and 10")

else:
    if (value > 0) and (value <= 10):
        print("you typed: ", value)
    else:
        print("the value you typed is incorrect!")



#type a number between 1 and 10: >? alpha
#you must type a number between 1 and 10

try:
    value = int(input('enter value between 1 and 10:'))
except:
    print ("you must enter a value between 1 and 10")
else:
    if (value > 0 ) and (value <=10):
        print("you typed: ",value)
    else:
        print("The value is less than 1 or more than 10")

# multiple exceptions, one except
try:
    value = int(input('enter value between 1 and 10:'))
except (ValueError,KeyboardInterrupt):
    print ("you must enter a value between 1 and 10")
else:
    if (value > 0 ) and (value <= 10):
        print("you typed: ", value)
    else:
        print("The value is less than 1 or more than 10")

# multiple exceptions, many excepts
try:
    value = int(input('enter value between 1 and 10:'))
except ValueError:
    print ("you must enter a value between 1 and 10")
except KeyboardInterrupt:
    print ("you must enter a value between 1 and 10")

else:
    if (value > 0 ) and (value <= 10):
        print("you typed: ", value)
    else:
        print("The value is less than 1 or more than 10")



# raising your own exceptions

try:
    Ex = ValueError()
    Ex.strerror = "Value must be between 1 and 10"
    raise Ex
except ValueError as e:
    print("ValueError Excpetion",e.strerror)
    sys.exit()   # carefull, this will halt execution.
finally:
    print("cleanup")

"""
for i = 1 to 100 do {
     if ( i % 3 ==0 && i % 5 ==0)
         print 'FizzBuzz'
     else if ( i % 3 == 0 )
         print 'Fizz'
     else if ( i % 5 == 0 )
         print 'Buzz'
     else
          print i
   }

"""

for x in range(1,100):
    if ( x % 3 == 0) and (x % 5 == 0):
        print ('FizzBuzz ', x)
    elif (x % 3 == 0):
        print ('Fizz ', x)
    elif (x % 5 == 0):
        print ('Buzz ', x)
    else:
        print(x)

"""
// missing element quiz
// list of n integers ... range 1 to n+1
// no duplicates
// what is the quickest way to find the missing integer?
// allocate an array of size n+1

// loop through the i/p assign array[j] = ip[j] (increment j)
// loop through and find the missing one still -1

// assume ip
// loop through make all -1
dim arr[n+1]
for i = 1 to n+1
   arr[i] = -1

for j = 1 to n
    arr[ ip[j]] = 1

for i=1 to n+1
  if arr[i] == -1
      print 'you are missing : ' , i
      break
"""




def find_missing(ip):
    """
    list of n integers ... range 1 to n+1
    no duplicates
    what is the quickest way to find the missing integer?
    """

    n = len(ip)
    print(ip)
    a = []

    # init
    for i in range(n+1):
        print (i)
        a.append(-1)

    print(a)

    print('----')
    # scan
    for i in range(n):
        print(i+1)
        a[ip[i+1]] = 1

    print('----')
    # locate missing integers
    for i in range(n+1):
        print(i)
        if (a[i] == -1):
            print('missing entry', i)

    return
find_missing([1,2,4,5,6,7,8,9])

# pydoc3 -p 8000
# /Library/Frameworks/Python.framework/Versions/3.4/bin
# http://localhost:8000/
# http://localhost:8000/get?key=print   (search for information on print)
# http://localhost:8000/print   (search for information on print)


# or
# pydoc -p 8000
# http://localhost:8000/
# http://localhost:8000/print   (search for information on print)


#chapter 11 - strings
#
print('Hello there (single quote)')
print("Hello there (double quote)")
print("""Triple quote
across several lines, you can also
use triple single quotes.""")

print ("""
This might be a nice way to have a little
01234567890123456789012345678901234567890123456789
01234567890123456789012345678901234567890123456789
01234567890123456789012345678901234567890123456789
""")

#
# special characters
# control - characters to how stuff is displayed... eg) tab
# accented - characters with an accent, like a ^
# drawing - character art
# typographical - special characters like pilcrow
# other - dependant on the character set you use.

# escape sequences are used to display special characters.
# \\ backslash
# \'  or \"
# \a
# \b
# \f
# \n
# \r
# \t
# \uhhhh - unicode character
# \v vertical tab
# \ooo - character from octal
# \xhh - character from hex

print("one line \r\nnext line")
print("accented A: \xC0")
print("a drawing character: \u2562")
print("a pilcrow: \266")
print("a division sign: \xF7")
"""
one line
next line
accented A: À
a drawing character: ╢
a pilcrow: ¶
a division sign: ÷
"""

# selecting individual characters

s1 = "Hello World"
s2 = "Python is fun!"

print (s1[0])
print (s1[0:5])
print (s1[:5])
print (s1[6:])

s3 = s1[:6] + s2[:6]
print (s3)

print(s2[:7]*5)

"""
H
Hello
Hello
World
Hello Python
Python Python Python Python Python
"""

# tools for manipulating strings
# there are a fair number of these!
"""
capitalize()
center(width, fillchar=" ")
expandtabs(tabsize=8)
isalnum()
isalpha()
isdececimal()
isdigit()
islower()
isnumeric()
isspace()
istitle()
isupper()
join(seq)
len(string)
ljust(width, fillchar-" ")
lower()
lstrip()
max(str)
min(str)
rjust(width, fillchar=" ")
rstrip()
split(str=" ", num=string.count(str))
splitlines(num=string.count('\n'))
strip()
swapcase()
title()
upper()
zfill(width)

"""

mystring = "    Hello World     "

print(mystring.upper())

print(mystring.strip())
print(mystring.center(21,"*"))
print(mystring.strip().center(21,"*"))

print(mystring.isdigit())
print(mystring.istitle())

print(max(mystring))

print(mystring.split())
print(mystring.split()[0])

"""
   HELLO WORLD
Hello World
*    Hello World
*****Hello World*****
False
True
r
['Hello', 'World']
Hello

"""


# locating a value in a string
# count(str, beg=0, end=len(string))
# endswith(suffix, beg=0, end=len(string))
# find(str, beg=0,end=len(string))
# index(str,beg=0, end=len(string))
# replace(old, new [, max])
# rfind(str, beg=0, end=len(string))
# rindex(str,beg=0,end=len(string))
# startswith(prefix, beg=0, end=len(string))

searchme = "The apple is red and the berry is blue!"

print (searchme)
print(searchme.find("is"))
print(searchme.rfind("is"))

print(searchme.count("is"))

print(searchme.startswith("The"))
print(searchme.endswith("The"))

print(searchme.replace("apple", "car").replace("berry","truck"))
"""
The apple is red and the berry is blue!
10
31
2
True
False
The car is red and the truck is blue!
"""

#formatting strings; a number of ways
# [[fill] align][sign][#][0][width][,][.precision][type]
#
# fill : fill character when there are not enough
# align: left <:  right >:  center ^: justified =:
# sign: + - or space
# # use alternative number format (0x)
# 0 sign aware and padded with 0s
# width
# , thousands seperator
# .precision characters past the decimal
# type String s, Integer b c d o x X n, Floating e E f F g G n %

#examples
formatted = "{:d}"
print (formatted.format(7000))

formatted = "{:,d}"
print (formatted.format(7000))

formatted = "{:^15,d}"
print (formatted.format(7000))

formatted = "{:*^15,d}"
print (formatted.format(7000))

formatted = "{:*^15.2f}"
print (formatted.format(7000))

formatted = "{:*>15X}"
print (formatted.format(7000))

formatted = "{:*<#15X}"
print (formatted.format(7000))

formatted = "A {0} {1} and a {0} {2}."
print(formatted.format("blue", "car", "truck"))

"""
7000
7,000
     7,000
*****7,000*****
****7000.00****
***********1B58
0X1B58*********
A blue car and a blue truck.
"""

# chapter 12 Managing Lists

list1 = ["one",1,"two",True]
print(list1)
dir(list1)

# append
# clear
# copy
# count
# extend
# index
# insert
# pop
# remove
# reverse
# sort

list1[1]
# 1
list[1:3]
# [1,'two']
list[1:]
# [1,'two',True]

# modifying lists
list1 = []
len(list1)
# 0
list1.append(1)
len(list1)
# 1
list1.insert(0,2)
print(list1)
# [2,1]

list2 = list1.copy()
list2
# [2, 1]

list1.extend(list2)
list1
# [2, 1, 2, 1]

list1.pop()
# 1
list1
# [2, 1, 2]

list1.remove(1)
list1
# [2, 2]

list1.clear()
list1
# []

# operators with lists
list1 = ["hello"] * 4
list1
# ['hello', 'hello', 'hello', 'hello']

list1 = ["hello"] + [" "] + ["world"]
print(list1)
# ['hello', ' ', 'world']

'hello' in list1
# True

# chapter 12 - strings ( see counter, search and sort)
# chapter 13 - data structures
# tuple -
# dictionary
# stack
# queue
# deque


# tuples
MyTuple = ("Red","Blue","Green")
print(type(MyTuple))
# <type 'tuple'>
MyTuple = MyTuple.__add__(("Purple",))
print(MyTuple)
# ('Red', 'Blue', 'Green', 'Purple')
MyTuple[2]
# 'Green'
MyTuple[2][3]
# 'e'

# dictionaries
colors = {"Sam":"Blue","Amy":"Red","Sarah":"Yellow"}
print(type(colors))
# <class 'dict'>
print(colors)
# {'Sarah': 'Yellow', 'Amy': 'Red', 'Sam': 'Blue'}
print(colors['Amy'])
# Red
for i in colors.keys():
    print("{0} likes the color {1}.".format(i,colors[i]))

"""
Sarah likes the color Yellow.
Amy likes the color Red.
Sam likes the color Blue.

"""



































































