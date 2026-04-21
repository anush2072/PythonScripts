'''
ou are given a 0-indexed array nums consisting of positive integers.

There are two types of operations that you can apply on the array any number of times:
    * Choose two elements with equal values and delete them from the array.
    * Choose three elements with equal values and delete them from the array.
Return the minimum number of operations required to make the array empty, or -1 if it is not possible.
'''
from typing import List
import math

def minOperations(nums: List[int]) -> int:
    cache = {}
    
    def minOps(num):
        if num in cache:
            return cache[num]
        if num in [2, 3]:
            return 1
        if num < 2:
            return -1

        x,y = minOps(num - 2), minOps(num - 3)
        if x > 0 and y > 0:
            cache[num] = min(x, y) + 1
        elif x > 0:
            cache[num] = x + 1  
        elif y > 0:
            cache[num] = y + 1
        else:
            cache[num] = -1

        return cache[num]

    counts = {}
    for num in nums:
        if num in counts.keys():
            counts[num] = counts[num]+1
        else:
            counts[num] = 1
    
    numOps = 0
    for key, count in counts.items():
        ops = minOps(count)
        if ops == -1:
            return -1
        else:
            numOps = numOps + ops
    
    return numOps

def minOperations_v2(nums: List[int]) -> int:
    counts = {}
    for num in nums:
        if num in counts:
            counts[num] = counts[num]+1
        else:
            counts[num] = 1
    
    result = 0
    for num, count in counts.items():
        if count == 1:
            return -1
        result = result + math.ceil(count / 3)
    
    return result

print(minOperations(nums = [2,3,3,2,2,4,2,3,4]))
print(minOperations(nums = [2,1,2,2,3,3]))

print(minOperations_v2(nums = [2,3,3,2,2,4,2,3,4]))
print(minOperations_v2(nums = [2,1,2,2,3,3]))

'''
=== TIME AND SPACE COMPLEXITY ===

minOperations (Dynamic Programming):
- Time Complexity: O(n * m)
  where n = length of nums array, m = maximum frequency of any number
  Building frequency map: O(n)
  For each unique number, computing minOps(count) with memoization: O(m)
  
- Space Complexity: O(m)
  Cache stores results for numbers from 2 to max frequency: O(m)
  Frequency map stores at most n entries: O(n), but n ≤ m in worst case

minOperations_v2 (Greedy):
- Time Complexity: O(n)
  Building frequency map: O(n)
  Single pass through frequency map: O(k) where k = number of unique elements ≤ n
  
- Space Complexity: O(k)
  Frequency map stores k entries where k = number of unique elements

=== ALGORITHM COMPARISON ===
DP Approach: Correct but slower, handles any operation sizes {2,3,x}
Greedy Approach: Optimal for {2,3} due to mathematical properties, faster
'''