'''
You are given two strings s and t consisting of only lowercase English letters.
Return the minimum number of characters that need to be appended to the end of s so that t becomes a subsequence of s.
A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.
'''
def appendCharacters(s: str, t: str) -> int:
    s_index, t_index = 0, 0
    
    # Find how many characters of t match s in order
    while s_index < len(s) and t_index < len(t):
        if s[s_index] == t[t_index]:
            t_index += 1
        s_index += 1
    
    # Characters from t that couldn't be matched need to be appended
    return len(t) - t_index

print(appendCharacters("coaching", "coding"))        
print(appendCharacters(s = "abcde", t = "a"))
print(appendCharacters(s="fff", t="ffff"))