"""
You are given 
    - an integer array coins representing coins of different denominations (e.g. 1 dollar, 5 dollars, etc) 
    - and an integer amount representing a target amount of money.

Return the fewest number of coins that you need to make up the exact target amount. If it is impossible to make up the amount, return -1.
You may assume that you have an unlimited number of each coin.
"""
from typing import List

def coinChange(coins: List[int], amount: int) -> int:
    coin_lookup = [amount + 1] * (amount + 1) # Initialize all dp[i] = amount + 1 (sentinel value meaning "impossible" - larger than any possible coin count)
    coin_lookup[0] = 0

    for a in range(1, amount + 1):
        for c in coins:
            if a - c >= 0:
                coin_lookup[a] = min(coin_lookup[a], 1 + coin_lookup[a - c])
    return coin_lookup[amount] if coin_lookup[amount] != amount + 1 else -1


print(coinChange([1,5,10], 12))
print(coinChange([2], 5))

'''
=== INTERVIEW FOLLOWUP QUESTIONS ===
1. How would you modify this solution to also return the actual coins used to make the amount?
2. What if you need to find the number of ways to make the amount instead of the minimum number of coins?

=== REAL WORLD APPLICATION ===
Vending Machine Systems: Used in automated payment systems to calculate the optimal combination of coins/bills to give as change, ensuring efficient cash dispensing while minimizing the number of physical currency units.

=== TIME AND SPACE COMPLEXITY ===
Time Complexity: O(n * m)
- n = amount, m = number of coin types
- Outer loop: O(n) for each amount from 1 to target
- Inner loop: O(m) for each coin type
- Overall: O(n * m)

Space Complexity: O(n)
- DP array of size amount + 1: O(n)
- No additional data structures used
- Could be optimized with space optimization techniques
'''