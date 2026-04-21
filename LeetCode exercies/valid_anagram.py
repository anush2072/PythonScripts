"""
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
"""
from collections import Counter

def is_anagram(s:str, t:str) -> bool:
    return Counter(s) == Counter(t)


# Alternate version 
def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    for char in t:
        if char not in count or count[char] == 0:
            return False
        count[char] -= 1
    return all(c == 0 for c in count.values())

# Test cases
print(is_anagram("listen", "silent"))
print(is_anagram("hello", "world"))
print(is_anagram("", ""))

'''
=== INTERVIEW FOLLOWUP QUESTIONS ===
1. How would you modify this solution to handle Unicode characters and emojis properly?
2. What if you need to check if two strings are anagrams when ignoring spaces and punctuation?

=== REAL WORLD APPLICATION ===
Password Security: Used in password strength validation to detect if a password is just a rearrangement of common words or previously used passwords, helping prevent weak password choices.

=== TIME AND SPACE COMPLEXITY ===
Time Complexity: O(n)
- Counter version: O(n) for building counters + O(k) for comparison where k = unique characters
- Manual version: O(n) for counting + O(n) for verification
- Overall: O(n) where n = length of strings

Space Complexity: O(k)
- Counter version: O(k) where k = number of unique characters
- Manual version: O(k) for the count dictionary
- In worst case (all unique characters): O(n)
'''