__author__ = 'steve1281'

import collections

MyDQ = collections.deque("abcdef",10)
print("Starting state:")
for i in MyDQ:
    print(i, end=' ')
print()
print('Appending and extending right')
MyDQ.append('h')
MyDQ.extend('ij')
for i in MyDQ:
    print(i, end=' ')
print()
print('MyDQ contains {0} items.'.format(len(MyDQ)))
print('Popping right')
print('Popping {0}'.format(MyDQ.pop()))
for i in MyDQ:
    print(i, end=' ')
print()
print('Appending and extending left')
MyDQ.appendleft('a')
MyDQ.extendleft('bc')
for i in MyDQ:
    print(i, end=' ')
print()
print('MyDQ contains {0} items.'.format(len(MyDQ)))
print('Popping Left')
print('Popping {0}'.format(MyDQ.popleft()))
for i in MyDQ:
    print(i, end=' ')
print()
print('Removing')
MyDQ.remove('a')
for i in MyDQ:
    print(i, end=' ')
print()

