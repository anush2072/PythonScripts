"""
Implement Insertion Sort and return intermediate states.

Insertion Sort is a simple sorting algorithm that builds the sorted list one element at a time, from left to right. It works by repeatedly taking an element from the unsorted portion and inserting it into its correct position in the sorted portion of the list.

Objective:

Given a list of key-value pairs, sort the list by key using Insertion Sort. Return a list of lists showing the state of the array after each insertion. If two key-value pairs have the same key, maintain their relative order in the sorted list.

Input:

pairs - a list of key-value pairs, where each key-value has an integer key and a string value. (0 <= pairs.length <= 100).
Example 1:

Input:
pairs = [(5, "apple"), (2, "banana"), (9, "cherry")]

Output:
[[(5, "apple"), (2, "banana"), (9, "cherry")], 
 [(2, "banana"), (5, "apple"), (9, "cherry")], 
 [(2, "banana"), (5, "apple"), (9, "cherry")]]
Notice that the output shows the state of the array after each insertion. The last state is the final sorted array. There should be pairs.length states in total.

Example 2:

Input:
pairs = [(3, "cat"), (3, "bird"), (2, "dog")]

Output:
[[(3, "cat"), (3, "bird"), (2, "dog")], 
 [(3, "cat"), (3, "bird"), (2, "dog")],
 [(2, "dog"), (3, "cat"), (3, "bird")]]
In this example, you can observe that the pairs with key=3 ("cat" and "bird") maintain their relative order, illustrating the stability of the Insertion Sort algorithm.
"""
# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        result = []
        for i in range(len(pairs)):
            key = pairs[i]
            j = i - 1
            while j >= 0 and pairs[j].key > key.key:
                pairs[j + 1] = pairs[j]
                j -= 1
            pairs[j + 1] = key
            result.append([p for p in pairs])
        return result

'''
=== INTERVIEW FOLLOWUP QUESTIONS ===
1. How would you modify this solution to handle very large datasets where storing all intermediate states becomes memory-intensive?
2. What if you need to implement insertion sort in-place without using extra space for the result array?

=== REAL WORLD APPLICATION ===
Real-time Data Streaming: Used in systems that process live data feeds where maintaining the order of arrival is crucial, such as stock market tickers or sensor data processing, helping maintain sorted views while preserving insertion order for equal elements.

=== TIME AND SPACE COMPLEXITY ===
Time Complexity: O(n²)
- Outer loop: O(n) iterations
- Inner while loop: O(n) in worst case (reverse sorted)
- Overall: O(n²) comparisons and shifts

Space Complexity: O(n²) for result array
- Result array stores n copies of the array: O(n²)
- In-place sorting would be O(1) extra space
- Each state snapshot requires O(n) space
'''
