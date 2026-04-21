from collections import Counter
from typing import List

def topKFrequent_v1(nums: List[int], k: int) -> List[int]:
    '''
    Returns all items with frequency ≥ k
    Example: [1,1,1,2,2,2,3,3], k=2 → [1, 2, 3] (frequency >= 2)
    '''
    frequency = Counter(nums)
    return [item for item, count in frequency.items() if count >= k]


def topKFrequent_v2(nums: List[int], k: int) -> List[int]:
    '''
    Returns the k most frequent items
    Example: [1,1,1,2,2,2,3,3], k=2 → [1, 2] or [2, 1] (top 2 by frequency)
    '''
    frequency = Counter(nums)
    return [item for item, _ in frequency.most_common(k)]


print(topKFrequent_v1([1,1,1,2,2,2,3,3], 2))        
print(topKFrequent_v2([1,1,1,2,2,2,3,3], 2))        

'''
=== INTERVIEW FOLLOWUP QUESTIONS ===
1. How would you solve this problem in O(n) time without using built-in Counter.most_common()? (Hint: Use bucket sort)
2. What if you need to return the k most frequent elements in order of frequency (highest to lowest)?

=== REAL WORLD APPLICATION ===
Social Media Analytics: Used to identify trending topics, hashtags, or keywords by finding the most frequently mentioned terms in posts or comments, helping platforms surface popular content.

=== TIME AND SPACE COMPLEXITY ===
Time Complexity: O(n log k) for v1, O(n log k) for v2
- Building Counter: O(n)
- Filtering items: O(m) where m = unique elements
- most_common(k): O(m log k) where m = unique elements
- Overall: O(n + m log k), simplified to O(n log k)

Space Complexity: O(m)
- Counter stores m unique elements
- Result list stores at most m elements
- In worst case (all unique): O(n)
'''        