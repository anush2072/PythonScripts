'''
Given an integer array nums, reorder it such that nums[0] <= nums[1] >= nums[2] <= nums[3]....
'''
from typing import List
def wiggleSort(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    result = []
    nums = sorted(nums)
    index, l, r = 0, 1, len(nums)-1
    result.append(nums[0])
    from_right = True

    while l<r:
        if nums[l] == result[index]:
            result.append(nums[l])
            l = l+1
            index = index + 1
            from_right = True
        elif nums[r] == result[index]:
            result.append(nums[r])
            r = r-1
            index = index+1
            from_right = False
        if from_right:
            result.append(nums[r])
            r = r-1
            index = index+1
            from_right = False
        else:
            result.append(nums[l])
            l = l+1
            index = index + 1
            from_right = True
    
    return result

print(wiggleSort(nums = [3,5,2,1,6,4]))
print(wiggleSort(nums = [6,6,5,6,3,8]))
