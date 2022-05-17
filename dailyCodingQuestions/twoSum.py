# subtract to see if k is reached

# basic logic here is using subtraction compliment sums
# plugging in the difference is to make sure that are checking to see which 
# numbers in the array are a compliment to having the nums suttracted from k > nums:
# even if k can be < than nums[i] the logic would just push a negative number in the map 
# this wouldn't break the logic

def twoSum (inputArray, k):

    m = {}
    
    for num in inputArray:
        if num not in m:
            #storing the compliment number of k-num, if anything in nums is equal
            m[k-num]  = 1
        else:
            return True
    return False
            

def main ():
    nums = [10, 15, 3, 7]
    

    k = 17
    
    print(twoSum(nums, k))

main()
