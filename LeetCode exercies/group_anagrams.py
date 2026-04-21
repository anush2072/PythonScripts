from typing import List
from collections import defaultdict, Counter

def group_anagrams(strs: List[str]) -> List[List[str]]:
    anagram_map = defaultdict(list)
    for word in strs:
        key = tuple(sorted(Counter(word).items())) # Anagrams like "eat", "tea", "ate" all produce the same tuple key.
        anagram_map[key].append(word) # Adds the current word to its anagram group. Words with identical character counts get the same key and are grouped together.
    return list(anagram_map.values())


print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat", "eat"]))


"""
Additional notes:
Counter(word): Creates a dict of character counts.
    Example: "eat" → {'e': 1, 'a': 1, 't': 1}
.items(): Returns dict items as list of (key, value) pairs.
    Example: [('e', 1), ('a', 1), ('t', 1)]
sorted(...): Sorts the pairs by character (to ensure consistent order).
    Example: [('a', 1), ('e', 1), ('t', 1)]
tuple(...): Converts to an immutable tuple for use as dict key.
    Example: (('a', 1), ('e', 1), ('t', 1))
"""

'''
=== INTERVIEW FOLLOWUP QUESTIONS ===
1. How would you optimize this solution to use O(n*k) time instead of O(n*k log k) where k is average string length?
2. What if you need to group anagrams while preserving the original order of groups as they first appear?

=== REAL WORLD APPLICATION ===
Text Processing & Search Engines: Used in document analysis to group words with the same letters, helping in spell correction, word games, and linguistic research where letter patterns are more important than word meanings.

=== TIME AND SPACE COMPLEXITY ===
Time Complexity: O(n * k log k)
- n = number of strings, k = average string length
- For each string: Counter creation O(k), sorting O(k log k)
- Overall: O(n * k log k)

Space Complexity: O(n * k)
- Anagram map stores all strings: O(n * k)
- Counter objects for each string: O(k) per string
- Result list stores grouped strings: O(n * k)
'''