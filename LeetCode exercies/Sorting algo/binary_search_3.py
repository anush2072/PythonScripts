'''
You are given an array of length n which was originally sorted in ascending order. It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:

[3,4,5,6,1,2] if it was rotated 4 times.
[1,2,3,4,5,6] if it was rotated 6 times.
Given the rotated sorted array nums and an integer target, return the index of target within nums, or -1 if it is not present.

You may assume all elements in the sorted rotated array nums are unique
'''
def binarySearch(nums, target):
    l,r = 0, len(nums)-1

    while l<=r:
        m = (l+r) // 2
        if nums[m] == target:
            return m
        if nums[l] <= nums[m]:
            if nums[l] <=target < nums[m]:
                r=m-1
            else:
                l = m+1
        else:
            if nums[m] < target <= nums[r]:
                l=m+1
            else:
                r=m-1

    return -1

if __name__ == '__main__':
    print(binarySearch(nums = [3,4,5,6,1,2], target = 1))
    print(binarySearch(nums = [3,5,6,0,1,2], target = 4))
    print(binarySearch(nums = [4,5,6,7,0,1,2], target = 0))