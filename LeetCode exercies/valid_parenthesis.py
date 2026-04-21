"""
You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type
"""
def isValid(s: str) -> bool:
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping:
            top = stack.pop() if stack else '#'
            if mapping[char] != top:
                return False
        else:
            stack.append(char)
    return not stack

print(isValid("([{}])"))
print(isValid(""))
print(isValid("[]"))
print(isValid("[]))"))

'''
=== INTERVIEW FOLLOWUP QUESTIONS ===
1. How would you modify this solution to handle not just validation but also return the minimum number of insertions needed to make the string valid?
2. What if we need to find the longest valid parentheses substring instead of just validation?

=== REAL WORLD APPLICATION ===
Code Editors/IDEs: Used in syntax highlighting and code validation to ensure proper bracket matching in programming languages, helping developers catch syntax errors in real-time.

=== TIME AND SPACE COMPLEXITY ===
Time Complexity: O(n)
- Single pass through the string
- Each character is processed exactly once
- Stack operations (push/pop) are O(1)

Space Complexity: O(n)
- In worst case (all opening brackets), stack stores all n characters
- Mapping dictionary is constant space O(1)
'''

