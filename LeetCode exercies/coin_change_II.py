'''
You are given an integer array coins representing coins of different denominations (e.g. 1 dollar, 5 dollars, etc) and an integer amount representing a target amount of money.

Return the number of distinct combinations that total up to amount. 
If it's impossible to make up the amount, return 0.

You may assume that you have an unlimited number of each coin and that each value in coins is unique.
'''
from typing import List

def change(amount: int, coins: List[int]) -> int:
    result = [0]*(amount+1)
    result[0] = 1  # Base case: one way to make amount 0
    
    # Coins outside, amounts inside to count COMBINATIONS (not permutations)
    for coin in coins:
        for i in range(coin, amount+1):
            result[i] = result[i] + result[i-coin]
    
    return result[amount]

print(change(amount = 4, coins = [1,2,3]))
print(change(amount = 7, coins = [2,4]))

'''
=== INTERVIEW FOLLOWUP QUESTIONS ===
1. How would you modify this solution to also return the actual coins used to make the amount?

=== TIME AND SPACE COMPLEXITY ===
- Time Complexity: O(n * m)
  where n = amount, m = number of coins
  Outer loop: m coins, Inner loop: up to n iterations each
  
- Space Complexity: O(n)
  DP array of size amount+1

=== LOOP ORDER INSIGHT ===
- Coins outside, amounts inside = COMBINATIONS (order doesn't matter)
  Example: amount=4, coins=[1,2,3] → [1,1,1,1], [1,1,2], [2,2], [1,3] = 4 distinct ways 
  
- Amounts outside, coins inside = PERMUTATIONS (order matters)
  Example: amount=4, coins=[1,2,3] → [1,1,1,1], [1,1,2], [1,2,1], [2,1,1], [2,2], [1,3] = 6 sequences including different orderings of the same coins
  
- Rule: What depends on what? Amounts depend on available coins
'''