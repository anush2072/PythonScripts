"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.
The output should not contain any duplicate triplets. You may return the output and the triplets in any order.
"""

from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    '''
    Step-by-step breakdown:
    - Sort the array: nums.sort() - enables ordered search and duplicate handling.
    - Outer loop: for i in range(n - 2) - fix the first element nums[i].
        - if i > 0 and nums[i] == nums[i - 1]: continue - skip duplicate values for i to avoid duplicate triplets.
    - Two pointers setup: left = i + 1, right = n - 1 - search in nums[i+1..n-1].
    - Inner loop: while left < right - find pairs that sum to -nums[i].
        - total = nums[i] + nums[left] + nums[right]
        - If total == 0: Add triplet, then skip duplicates for left and right, then move both pointers.
        - If total < 0: Move left right (need larger sum).
        - If total > 0: Move right left (need smaller sum).
    '''
    nums.sort()
    result = []
    n = len(nums)
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left = i + 1
        right = n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return result

print(threeSum([-1,0,1,2,-1,-4]))
print(threeSum([0,1,1]))
print(threeSum([0,0,0]))

#  -----------------------------------------


def twoSum(nums: List[int], target: int) -> List[List[int]]:
    values_dict = {}
    result = []
    for i in range(len(nums)):
        required = target - nums[i]
        if required in values_dict:
            result.append([required, nums[i]])
        values_dict[nums[i]] = i
    return result  


def threeSum_v2(nums: List[int]) -> List[List[int]]:
    '''
    Still O(n²) time but with hash map overhead per call, uses O(n) space for the set of triplets,
    '''
    nums_copy = nums[:]  # Avoid modifying original
    nums_copy.sort()
    result = set()
    n = len(nums_copy)
    for i in range(n - 2):
        if i > 0 and nums_copy[i] == nums_copy[i - 1]:
            continue
        pairs = twoSum(nums_copy[i+1:], -nums_copy[i])
        for pair in pairs:
            triplet = tuple(sorted([nums_copy[i], pair[0], pair[1]]))
            result.add(triplet)
    return [list(t) for t in result]

print(threeSum_v2([-1,0,1,2,-1,-4]))
print(threeSum_v2([0,1,1]))
print(threeSum([0,0,0]))

'''
=== INTERVIEW FOLLOWUP QUESTIONS ===
1. How would you modify this solution to find all quadruplets that sum to a target (4-sum problem)?
2. What if you need to find the closest triplet sum to a target value instead of exactly zero?

=== REAL WORLD APPLICATION ===
Financial Portfolio Optimization: Used in investment management to find combinations of three assets that balance to zero risk exposure, helping create hedged investment strategies and balanced portfolios.

=== TIME AND SPACE COMPLEXITY ===
Time Complexity: O(n²)
- Sorting: O(n log n)
- Outer loop: O(n)
- Two-pointer inner loop: O(n) for each iteration
- Overall: O(n log n + n²) = O(n²)

Space Complexity: O(1) for main algorithm, O(k) for results
- Main algorithm uses constant extra space (ignoring output)
- Result set stores k triplets where k = number of valid solutions
- Sorting modifies input in-place
'''