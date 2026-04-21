'''
Given an array of integers nums, find the subarray with the largest sum and return the sum.
A subarray is a contiguous non-empty sequence of elements within an array.

Kadane's Algorithm: 
Kadane's Algorithm is based on one simple observation:
if the running sum becomes negative, keeping it will only reduce the sum of any future subarray
So whenever the current sum drops below zero, we reset it and start a new subarray from the next element
'''
from typing import List
def maxSubArray( nums: List[int]) -> int:
    maxSum, curSum = nums[0], 0
    for num in nums:
        if curSum < 0:
            curSum = 0
        curSum = curSum + num
        maxSum = max(maxSum, curSum)
    return maxSum

print(maxSubArray(nums = [2,-3,4,-2,2,1,-1,4]))
print(maxSubArray(nums = [-1]))

def maxSubArrayWithIndices(nums: List[int]) -> List[int]:
    maxSum, curSum = nums[0], 0
    start, end = 0, 0
    tempStart = 0
    
    for i, num in enumerate(nums):
        if curSum < 0:
            curSum = 0
            tempStart = i
        
        curSum = curSum + num
        
        if curSum > maxSum:
            maxSum = curSum
            start = tempStart
            end = i
    
    return nums[start:end+1]

def maxSubArrayWithIndices_v2(nums: List[int]) -> tuple[int, int, int]:
    maxSum, curSum = nums[0], 0
    start, end = 0, 0
    tempStart = 0
    
    for i, num in enumerate(nums):
        if curSum < 0:
            curSum = 0
            tempStart = i
        
        curSum = curSum + num
        
        if curSum > maxSum:
            maxSum = curSum
            start = tempStart
            end = i
    
    return maxSum, start, end

print("Subarray:", maxSubArrayWithIndices(nums = [2,-3,4,-2,2,1,-1,4]))
print("With indices:", maxSubArrayWithIndices_v2(nums = [2,-3,4,-2,2,1,-1,4]))