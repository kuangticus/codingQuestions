#Time Complexity is O(logN) - We are starting using the half of the array that closet to number always
#Space Complexity is O(1)

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


def main ():
    # given a acended sorting list define binary search function iteratively and rescursively
    nums = [1,2,3,4,9,8,19,20]
    target = 19

    print(nums)
    l, r = 0, len(nums) - 1

    print(binarySearch(nums, target, l, r))

main()