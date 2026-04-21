'''Given two strings text1 and text2, 
return the length of the longest common subsequence between the two strings if one exists, 
otherwise return 0.

A subsequence is a sequence that can be derived from the given sequence by deleting some or no elements without changing the relative order of the remaining characters.

For example, "cat" is the longest common subsequence of "calt" and "crabt"
'''
# region - BruteForce approach
def longestCommonSubsequence_v1(text1: str, text2: str) -> int:
    def dfs(i,j):
        if i == len(text1) or j == len(text2):
            return 0
        if text1[i] == text2[j]:
            return 1 + dfs(i+1,j+1)
        return max(dfs(i+1,j), dfs(i,j+1))
    return dfs(0,0)

print(longestCommonSubsequence_v1(text1 = "cat", text2 = "crabt" ))
print(longestCommonSubsequence_v1(text1 = "calt", text2 = "crabt" ))
print(longestCommonSubsequence_v1(text1 = "abcd", text2 = "abcd"))
print(longestCommonSubsequence_v1(text1 = "abcd", text2 = "efgh"))
'''
=== BRUTE FORCE COMPLEXITY ===
- Time Complexity: O(2^(m+n))
  At each step, we have 2 choices: move in text1 or text2
  In worst case, we explore all possible subsequences
  
- Space Complexity: O(m+n)
  Recursion stack depth goes up to m+n in worst case
  No additional data structures used

'''
# endregion  - BruteForce approach


# region - dynamic programming
'''
'''
def longestCommonSubsequence_v2(text1: str, text2: str) -> int:
    lookup = {}
    def dfs(i,j):
        if i == len(text1) or j == len(text2):
            return 0
        if (i,j) in lookup:
            return lookup[(i,j)]
        if text1[i] == text2[j]:
            lookup[(i, j)] = 1 + dfs(i + 1, j + 1)
        else:
            lookup[(i,j)] = max(dfs(i + 1, j), dfs(i, j + 1))
        
        return lookup[(i, j)]
    
    return dfs(0,0)
print(longestCommonSubsequence_v2(text1 = "cat", text2 = "crabt" ))
print(longestCommonSubsequence_v2(text1 = "calt", text2 = "crabt" ))
print(longestCommonSubsequence_v2(text1 = "abcd", text2 = "abcd"))
print(longestCommonSubsequence_v2(text1 = "abcd", text2 = "efgh"))
print(longestCommonSubsequence_v2(text1="ylqpejqbalahwr", text2="yrkzavgdmdgtqpg"))
'''
=== DYNAMIC PROGRAMMING COMPLEXITY ===
- Time Complexity: O(m * n)
  Each unique (i,j) pair is computed once using memoization
  Total pairs = m * n

- Space Complexity: O(m * n)
  Memoization dictionary stores up to m * n entries
  Recursion stack depth: O(m+n)
  Can be optimized to O(min(m,n)) with bottom-up DP

'''
# endregion - dynamic programming


'''
=== PERFORMANCE COMPARISON ===
- Brute Force: Exponential time, only works for very small strings
- DP with Memoization: Polynomial time, works for moderate strings
- Bottom-up DP: Same time, better space control

=== SPACE OPTIMIZATION OPPORTUNITY ===
- Use 2D DP array instead of dictionary for O(1) lookup
- Further optimize to O(min(m,n)) using rolling array technique
- Bottom-up approach eliminates recursion overhead
'''