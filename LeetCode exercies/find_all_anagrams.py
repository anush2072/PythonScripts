'''
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

 

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
'''
def findAnagrams(s, p):
    result = []
    
    # Sort the pattern once
    sorted_p = sorted(p)
    n = len(p)
    
    # Scan main string in batches of length p
    for i in range(len(s) - n + 1):
        batch = s[i:i+n]
        if sorted(batch) == sorted_p:
            result.append(i)
    
    return result


print(findAnagrams("cbaebabacd", "abc"))
print(findAnagrams("ababcbasdba", "ab"))
print(findAnagrams("abab", "ca"))

'''
=== INTERVIEW FOLLOWUP QUESTIONS ===
1. How would you optimize this solution to avoid sorting each substring? (Hint: Use sliding window with character frequency counts)
2. What if the input contains Unicode characters or emojis? How would you handle that?

=== REAL WORLD APPLICATION ===
Plagiarism Detection: This algorithm can be used to detect paraphrased content by finding anagrammatic phrases in documents, helping identify potential plagiarism even when word order is changed.

=== TIME AND SPACE COMPLEXITY ===
Time Complexity: O((n-m+1) * m log m)
- Where n = len(s), m = len(p)
- Sorting pattern p: O(m log m)
- For each of (n-m+1) positions: extract substring O(m), sort O(m log m), compare O(m)

Space Complexity: O(m + k)
- O(m) for sorted pattern and temporary batch
- O(k) for result array where k = number of matches found
'''