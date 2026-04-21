'''
Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without duplicate characters.

A substring is a contiguous sequence of characters within a string.
'''
def lengthOfLongestSubstring(s: str) -> int:
    char_set = set()
    left = 0
    max_len = 0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)
    return max_len

print(lengthOfLongestSubstring('zxyzxyz'))

'''
=== INTERVIEW FOLLOWUP QUESTIONS ===
1. How would you modify this solution to return the actual longest substring instead of just its length?
2. What if you need to find the longest substring with at most K distinct characters instead of all unique characters?

=== REAL WORLD APPLICATION ===
DNA Sequence Analysis: Used in bioinformatics to find the longest unique sequence patterns in DNA strings, helping identify genetic markers and mutations for medical research.

=== TIME AND SPACE COMPLEXITY ===
Time Complexity: O(n)
- Each character is visited at most twice (once by right pointer, once by left pointer)
- Set operations (add/remove) are O(1) on average
- Overall single pass through the string

Space Complexity: O(min(n, m))
- Set stores at most the size of the current window
- In worst case (all unique characters): O(n)
- Where m = size of character set (ASCII/Unicode)
'''