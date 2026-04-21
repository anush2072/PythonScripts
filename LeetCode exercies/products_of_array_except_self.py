"""
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].
Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in  O(n) time without using the division operation?
"""
from typing import List
import math


# Version 1 : Solution with division (O(n) time)
def productExceptSelf(nums: List[int]) -> List[int]:
    total_product = math.prod(nums)
    zero_count = nums.count(0)
    output = [0] * len(nums)

    if zero_count > 1:
        return output  # All 0

    if zero_count == 1:
        # Only the zero position gets the product of others
        non_zero_product = math.prod(x for x in nums if x != 0)
        zero_index = nums.index(0)
        output[zero_index] = non_zero_product
    else:
        for i, num in enumerate(nums):
            output[i] = total_product // num

    return output

print(f"V1(With Divison) : {productExceptSelf([1,2,4,6])}")   
'''
=== TIME AND SPACE COMPLEXITY ===
Time Complexity: O(n)
- Calculating total product: O(n)
- Counting zeros: O(n)
- Building output array: O(n)
- Overall: O(n)

Space Complexity: O(n)
- Output array: O(n)
- No additional data structures used
- Could be optimized to O(1) extra space by modifying output in-place
'''


# Version 2: Solution without division (O(n) time)
def productExceptSelf_WithoutDivison(nums: List[int]) -> List[int]:
    n = len(nums)
    result = [0]*n
    prefix = [0]*n
    suffix = [0]*n

    prefix[0] = suffix[n-1] = 1

    for i in range(1,n):
        prefix[i] = prefix[i-1] * nums[i-1]
    
    for j in range(n-2, -1, -1):
        suffix[j] = suffix[j+1] * nums[j+1]
    
    for k in range(n):
        result[k] = prefix[k] * suffix[k]
    
    return result

print(f"V2(Without Divison) : {productExceptSelf_WithoutDivison([1,2,4,6])}")   
'''
=== TIME AND SPACE COMPLEXITY ===
Time Complexity: O(n)

Space Complexity: O(n)
- We can compute the product of all elements except the current one without using extra prefix and suffix array ?
'''


#  ***************************


'''
=== INTERVIEW FOLLOWUP QUESTIONS ===
1. How would you implement the O(n) solution without division using prefix and suffix products?
2. What if the input array is very large and you need to optimize space usage to O(1) extra space?

=== REAL WORLD APPLICATION ===
Financial Risk Analysis: Used in portfolio management to calculate the impact of removing one asset from a diversified portfolio, helping analysts understand how each individual asset contributes to overall portfolio performance and risk.
'''
