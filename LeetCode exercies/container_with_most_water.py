"""
You are given an integer array heights where heights[i] represents the height of the i_th bar
Return the maximum amount of water a container can store.

You may choose any two bars to form a container. 
For each pair (i, j), the height of the container is the shorter of the two lines, and the width is the distance between them.


Context:
Two Pointers Technique - Moving pointers from opposite ends of an array to efficiently search for optimal pairs
"""
from typing import List

def maxArea(heights: List[int]) -> int:
    result = 0
    left = 0
    right = len(heights) - 1
    while left < right:
        height = min(heights[left], heights[right])
        width = right - left
        area = width * height
        result = max(result, area)
        if heights[left] < heights[right]:
            left = left + 1
        else:
            right = right - 1

    return result

print(maxArea([1,7,2,5,4,7,3,6]))
print(maxArea([2,2,2]))

'''
=== INTERVIEW FOLLOWUP QUESTIONS ===
1. How would you modify this solution to return the actual indices of the two lines that form the maximum area container?
2. What if you need to find the maximum area container that can hold exactly a given amount of water?

=== REAL WORLD APPLICATION ===
Urban Planning: Used in city design to optimize placement of buildings and structures to maximize usable space between them, helping architects and planners efficiently utilize land in dense urban environments.

=== TIME AND SPACE COMPLEXITY ===
Time Complexity: O(n)
- Single pass with two pointers moving towards each other
- Each element is processed exactly once
- Constant time operations within the loop

Space Complexity: O(1)
- Only a few variables (left, right, result) used
- No additional data structures created
- Input array is not modified
'''
