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






























