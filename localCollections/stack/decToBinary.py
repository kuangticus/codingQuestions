"""
Convert Decimal number into binary string eqivalent
"""

from stack import Stack

def convertDec(plngDecimalInput):

    binary = Stack()

    divided = plngDecimalInput

    while divided >= 1:
        binary.push(divided % 2)
        divided = divided//2    

    binaryString = ""
    while not binary.isEmpty():
        binaryString += str(binary.pop())

    return binaryString

decimal = 12
print(convertDec(decimal))

