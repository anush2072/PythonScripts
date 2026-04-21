"""
We can also specify a custom sorting order by using the key parameter in the .sort() method. 
The key parameter doesn't accept a value, instead, it accepts a function that returns a value to be used for sorting.
"""
from typing import List

def get_word_length(word: str) -> int:
    return len(word)

def get_abs_value(number) -> int:
    return abs(number)

def sort_words(words: List[str]) -> List[str]:
    words.sort(key=get_word_length, reverse=True)
    return words

def sort_numbers(numbers: List[int]) -> List[int]:
    numbers.sort(key=get_abs_value)
    return numbers



print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))
print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))

'''
=== INTERVIEW FOLLOWUP QUESTIONS ===
1. How would you implement custom sorting with multiple criteria (e.g., sort by length first, then alphabetically)?
2. What if you need to sort complex objects like dictionaries or custom classes based on specific attributes?

=== REAL WORLD APPLICATION ===
E-commerce Platforms: Used in product catalog management to sort items by various criteria like price, rating, popularity, or relevance, helping users find products that best match their preferences and needs.

=== TIME AND SPACE COMPLEXITY ===
Time Complexity: O(n log n)
- Python's sort uses Timsort algorithm
- Key function calls: O(n) total
- Sorting comparisons: O(n log n)
- Overall: O(n log n) where n = number of elements

Space Complexity: O(n) for Timsort
- Timsort requires O(n) auxiliary space in worst case
- Key function results may be cached: O(n)
- In-place sorting modifies original array
'''
