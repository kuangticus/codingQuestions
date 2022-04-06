"""
Program that determines if parenthesis are closed and balanced
"""

from stack import Stack

def isBalanced(pstrInputString):

    eval = Stack()

    isBalance = True

    for par in pstrInputString:
        if not isBalance:
            break
            
        if par in "{[(":
            eval.push(par)
        else:
            if eval.isEmpty():
                isBalance = False
            else:
                if not isMatch(eval.pop(), par):
                    isBalance = False

    if isBalance and eval.isEmpty:
        return True
    else:
        return False

def isMatch(pstrParen1, pstrParen2):

    if pstrParen1 == '[' and pstrParen2 == ']':
        return True
    elif pstrParen1 == '(' and pstrParen2 == ')':
        return True
    elif pstrParen1 == '{' and pstrParen2 == '}':
        return True
    else:
        return False

def main():
    args = input("Input Parentheis, bracket, braces string for balance eval: \n")
    if isBalanced(args):
        print( args, " is balanceed")
    else:
        print(args, " is not balanced")

main()