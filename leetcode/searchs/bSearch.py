
'''
#Time Complexity is O(logN) - We are starting using the half of the array that closet to number always
#Space Complexity is O(1)
#Iterative method
'''

def binarySearch(nums, target, left , right):
    while right >= left:
        # we need to use the pivot for this
        # pivot that is calculated is got towards the number we are querying
        pivot = left  + (right-left) // 2
        print(nums[pivot], end = ',')

        if nums[pivot] == target:
            return pivot
        
        elif target > nums[pivot]:
            left = pivot+1
        else:
            right = pivot-1
    return -1

    