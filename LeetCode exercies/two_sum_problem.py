"""
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.
"""
from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    values_dict = {}
    for i in range(len(nums)):
        required = target - nums[i]
        if required in values_dict:
            return [values_dict[required], i]
        else:
            values_dict[nums[i]] = i

    return None   

# Example Usage:
my_list = [3,4,5,6]
goal = 7
output = twoSum(my_list, goal)
print(f"Input: {my_list}, goal: {goal}")
print(f"Output: {output}")

'''
=== INTERVIEW FOLLOWUP QUESTIONS ===
1. What if the input has multiple pairs that sum to the target? How would you modify the solution to return all pairs?
2. How would you solve this problem if you need to find three numbers that sum to the target (3-sum problem)?

=== REAL WORLD APPLICATION ===
Financial Trading: Used in algorithmic trading to find pairs of stocks or assets that complement each other in a portfolio, where the combined value meets a specific investment target while balancing risk.

=== TIME AND SPACE COMPLEXITY ===
Time Complexity: O(n)
- Single pass through the array
- Dictionary lookups are O(1) on average

Space Complexity: O(n)
- Dictionary stores up to n elements in the worst case
- Each element is stored once as we iterate through the array
'''

