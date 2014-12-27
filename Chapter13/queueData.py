__author__ = 'steve1281'

import queue

MyQueue = queue.Queue(3)

print(MyQueue.empty())

input("Press any key")

MyQueue.put(1)
MyQueue.put(2)
print(MyQueue.full())
input("Press any key")

MyQueue.put(3)
print(MyQueue.full())
input("Press any key")

print(MyQueue.get())
print(MyQueue.empty())
print(MyQueue.full())
input("Press any key")

print(MyQueue.get())
print(MyQueue.get())



