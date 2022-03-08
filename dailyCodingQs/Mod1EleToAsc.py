
# Coding question for modifying One element at max to achieve non decreasing or ascending order

def optMakeAscending():

    return None

# Time Complexity: O(n) - runs through the inputed array 1 time
# Space Complexity: O(1) - constant space since we don't make anything

def nonOptmakeAscending(inputArray):
    
    swap = 0
    # Base cases: first and last and empty
    
    # if the length of the array is 0
    if len(inputArray) == 0:
        return False

    # if the first element is bigger than the second one then swap
    if inputArray[0] > inputArray[1]:
        inputArray[0], inputArray[1] = inputArray[1], inputArray[0]
        swap += 1

    # if the last element is least then the second to last element swap
    if inputArray[-1] < inputArray[-2]:
        inputArray[-1], inputArray[-2] = inputArray[-2], inputArray[-1]
        swap += 1
    
    # for the rest of the elements swap if the next previous element is > than the next
    for i in range(1,len(inputArray)-1):
        if inputArray[i] > inputArray[i+1]:
            inputArray[i], inputArray[i+1] = inputArray[i+1], inputArray[i]
            swap += 1

    # if swapped more than once then False 
    return (swap == 1 or swap == 0)


def main():

    # call  makeAscending() ]

    testArray = [1, 3, 2, 5]
    testArray1  = [1, 5, 3, 6, 2]
    

    print("Non Optimized: " , nonOptmakeAscending(testArray1))

main()