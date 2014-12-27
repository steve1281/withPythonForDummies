__author__ = 'steve1281'

MyStack = []
StackSize = 3

def DisplayStack():
    print("Stack currently contains:")
    for Item in MyStack:
        print(Item)


def Push(Value):
    if len(MyStack) < StackSize:
        MyStack.append(Value)
    else:
        print("Stack is full!")


def Pop():
    if len(MyStack)>0:
        MyStack.pop()
    else:
        print("Stack is empty.")

Push(1)
Push(2)
Push(3)
DisplayStack()
input("Press any key")

Push(4)
DisplayStack()
input("Press any key")

Pop()
DisplayStack()
input("Press any key")

Pop()
Pop()
Pop()
DisplayStack()

