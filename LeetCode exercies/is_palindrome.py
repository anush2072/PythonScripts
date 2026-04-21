import re
def isPalindrome(s: str) -> bool:
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()    
    print(s)
    n = len(s)
    for i in range(n):
        if(s[i]!= s[n-i-1]):
            return False
    return True

print(isPalindrome("Was it a car or a cat I saw?"))

'''
=== INTERVIEW FOLLOWUP QUESTIONS ===
1. How would you optimize this solution to use O(1) space without creating a new string?
2. What if you need to check if a string is a palindrome when considering only letters (ignoring numbers and symbols)?

=== REAL WORLD APPLICATION ===
Natural Language Processing: Used in chatbot and voice assistant systems to detect palindromic phrases, helping with language games, educational tools, and pattern recognition in text analysis.

=== TIME AND SPACE COMPLEXITY ===
Time Complexity: O(n)
- Regex cleaning: O(n) to process each character
- Palindrome check: O(n/2) comparisons, simplified to O(n)
- Overall: O(n) where n = length of input string

Space Complexity: O(n)
- New cleaned string created: O(n) in worst case
- No additional data structures used
- Could be optimized to O(1) by using two-pointer approach on original string
'''