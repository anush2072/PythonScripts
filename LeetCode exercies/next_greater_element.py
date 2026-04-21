'''
The next greater element of some element x in an array is the first greater element that is to the right of x in the array.

You are given two 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2. nums2 contains unique elements.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. 
If there is no next greater element, then the answer for this query is -1.

Example 1:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2]

Output: [-1,3,-1]
Explanation:

There is no next greater element for 4.
3 is the next greater element for 1.
There is no next greater element for 2.
Example 2:

Input: nums1 = [2,4], nums2 = [1,2,3,4]

Output: [3,-1]
Explanation:

3 is the next greater element for 2.
There is no next greater element for 4.
'''
from typing import List, Optional

def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
    result = []

    for num1 in nums1:
        next_greatest = -1
        for i in range(len(nums2)-1, -1, -1):
            if nums2[i] == num1:
                break
            if nums2[i] > num1:
                next_greatest = nums2[i]
        result.append(next_greatest)

    return result

print(nextGreaterElement([2,4], [1,2,3,4]))
print(nextGreaterElement(nums1 = [4,1,2], nums2 = [1,3,4,2]))
print(nextGreaterElement(nums1 = [7,1,5,3,6,4], nums2 = [7,1,5,3,6,4]))
print(nextGreaterElement(nums1 = [1,2,3,4,5], nums2 = [1,2,3,4,5]))

'''
=== INTERVIEW FOLLOWUP QUESTIONS ===
1. How would you optimize this solution using a stack to achieve O(n + m) time complexity?
2. What if nums2 contains duplicate elements? How would you modify the solution?
3. Can you solve this problem in a single pass through nums2 using a monotonic stack?

=== REAL WORLD APPLICATION ===
Stock Price Analysis: In financial markets, this algorithm helps find the next higher price point for each stock price in a given time series. This is useful for identifying resistance levels and potential profit-taking opportunities for traders.

Dependency Management: In software package managers, this helps determine which version of a dependency comes next in the version hierarchy. When upgrading packages, it identifies the next compatible higher version for each current version.

=== TIME AND SPACE COMPLEXITY ===
Time Complexity: O(n * m)
- n = length of nums1, m = length of nums2
- For each element in nums1, we potentially scan through all of nums2
- Worst case: O(n * m) when each num1 is at the end of nums2
- Best case: O(n) when each num1 is at the beginning of nums2

Space Complexity: O(1)
- Only using a few variables (result list, next_greatest, loop counters)
- No additional data structures that grow with input size
- The result list of size n is required for output, not counted as extra space

Note: This can be optimized to O(n + m) time using a stack-based approach with a hash map for preprocessing.
'''