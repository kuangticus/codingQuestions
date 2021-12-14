
# check if string is balanced: now it removes all of the the necessary parens to create a balances paren tree

# Time Complexity: O(n) since we are looping one time through inputString
# Space Complexity: O(1) nothing new is allocated other than tracking variables. 

# Returns the minimum number to balance

# input: inputString for parenthesis
def minParenRM(inputString):
    minRm = 0
    openCount = 0

    #loop one time through input String
    for char in inputString:

        #track the opened parenthesis
        if char not in ('(',')'):
            print("Input String is not only parenthesis", end = ' ')
            return -1
        if char == '(':
            openCount += 1
        # if we don't have open parenthesis and there is close automatically remove it
        elif char == ')' and openCount == 0:
            openCount -= 1
        else:
            openCount -= 1

    # return the absolute value if we 
    return abs(openCount)

def main ():

    parenStr = "((((((s f("

    print("Function 1: ", end = '')
    print(minParenRM(parenStr))


main()