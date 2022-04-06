"""
Program to reverse string using Stack instead of [::-1]
"""
from stack import Stack

def reverseString(pstrInputString):

    stackString = Stack()

    for i in pstrInputString:

        stackString.push(i)
    
    reversed = ""
    while not stackString.isEmpty():

        reversed += stackString.pop()

    return reversed

def main():

    arg = input("What string you want to reverse? \n")

    print("Your reversed string is: ", reverseString(arg))

main()