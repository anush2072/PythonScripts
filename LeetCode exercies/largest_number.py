'''
You are given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.
 where the result is all zeros (return "0")
'''

from typing import List

def largestNumber(nums: List[int]) -> str:
    def compare(n1, n2):
        if n1 + n2 > n2+ n1:
            return -1
        else:
            return 1

    for i in range(len(nums)):
        nums[i] = str(nums[i])

    from functools import cmp_to_key
    nums = sorted(nums, key=cmp_to_key(compare))
    result = "".join(nums)

    if result[0] == '0':
        return '0'
    
    return result

print(largestNumber(nums = [10,2]))
print(largestNumber(nums = [3,30,34,5,9]))