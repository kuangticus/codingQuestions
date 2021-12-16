# uber question very simple and straightfoward

# bar raiser question: do it without divison
# answer would be to use binary long division

# assuming zeros don't exist in the input


def multArray(nums):
    multiple = 1
    result = []

    # getting the multiple 
    for i in nums:
        multiple *= i

    # divide the multiple by i to remove i from the multiple
    for i in nums:
        result.append(multiple//i)
        
    return result

def multArrayNoDiv(nums):



def main ():

    nums = [1, 2, 3, 4, 5]

    print( multArray(nums) )


main()