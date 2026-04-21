"""
# general syntax for slicing is sequence[start:stop:step]
"""

my_list = ['r', 'e', 'd', 'green', 'blue', 'alpha']
my_string = "Hello World"

# Elements from index 1 up to (but not including) index 4
print(my_list[1:4]) # Output: ['e', 'd', 'green']
print(my_string[1:4]) # Output: 'ell'

# The last two elements
print(my_list[-2:]) # Output: ['blue', 'alpha']
print(my_string[-2:]) # Output: 'ld'

# All elements except the last one
print(my_string[:-1]) # Output: 'Hello Worl'

# All elements except the first one
print(my_string[1:]) # Output: 'ello World'

# Every second element
print(my_list[::2]) # Output: ['r', 'd', 'blue']
print(my_string[::2]) # Output: 'HloWrd'

# Reverse the sequence
input_string = "bob"
reverse_string = input_string[::-1]
print(f"{input_string} is a palindrome: {input_string == reverse_string}")

'''
=== INTERVIEW FOLLOWUP QUESTIONS ===
1. How would you handle string slicing with Unicode characters and multi-byte characters that might be split incorrectly?
2. What if you need to implement efficient string slicing operations on very large strings where creating new substrings becomes memory-intensive?

=== REAL WORLD APPLICATION ===
Text Editors & IDEs: Used in code editors for syntax highlighting, auto-completion, and text manipulation operations like extracting method names, formatting code blocks, and implementing search/replace functionality.

=== TIME AND SPACE COMPLEXITY ===
Time Complexity: O(k) where k = length of slice
- Each slicing operation creates a new string
- Time proportional to slice length, not original string
- Step parameter affects complexity: O(k/step) for non-unit steps

Space Complexity: O(k) for each slice
- New substring created: O(k) where k = slice length
- Original string remains unchanged
- Multiple slices accumulate memory usage
'''
