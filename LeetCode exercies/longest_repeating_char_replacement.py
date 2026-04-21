'''
You are given a string s consisting of only uppercase english characters and an integer k. 
You can choose up to k characters of the string and replace them with any other uppercase English character.

After performing at most k replacements, return the length of the longest substring which contains only one distinct character.
'''
from collections import Counter

def characterReplacement(s: str, k: int) -> int:
    count = {}
    res = 0

    l = 0
    maxf = 0
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        maxf = max(maxf, count[s[r]])

        while (r - l + 1) - maxf > k:
            count[s[l]] -= 1
            l += 1
        res = max(res, r - l + 1)

    return res

print(characterReplacement("AAABABB", 1))
print(characterReplacement("XYYX", 2))

'''
=== INTERVIEW FOLLOWUP QUESTIONS ===
1. How would you modify this solution to return the actual substring instead of just the length?
2. What if we need to handle lowercase letters as well? How does that affect the space complexity?
3. Can you solve this using binary search instead of sliding window?
4. What if we have multiple queries on the same string - how would you optimize for repeated calls?

=== REAL WORLD APPLICATION ===
Text Editors/Word Processors: Used in auto-correction and text analysis features to find the longest sequence of similar characters that can be standardized with minimal edits, helping with spell checking and text normalization.

DNA Sequence Analysis: In bioinformatics, this algorithm helps identify the longest DNA segments that can be made uniform with minimal mutations, useful for pattern recognition in genetic sequences.

=== TIME AND SPACE COMPLEXITY ===
Time Complexity: O(n)
- Single pass through the string with sliding window
- Each character is processed at most twice (once when expanding, once when shrinking)
- Dictionary operations are O(1) average case

Space Complexity: O(1)
- Dictionary stores at most 26 entries (uppercase English letters)
- This is constant space regardless of input size
- If we support all ASCII characters, space becomes O(256) = O(1)
- If we support Unicode, space becomes O(k) where k is unique characters in string
'''

