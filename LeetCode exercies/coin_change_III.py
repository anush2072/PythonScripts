'''
You are given an integer array coins representing coins of different denominations and an integer amount.
Return ALL possible combinations of coins that total up to the amount.
If it's impossible to make up the amount, return an empty list.

You may assume that you have an unlimited number of each coin and that each value in coins is unique.
'''
from typing import List

def coinChangeCombinations(amount: int, coins: List[int]) -> List[List[int]]:
    # dp[i] stores all combinations that make amount i
    dp = [[] for _ in range(amount + 1)]
    dp[0] = [[]]  # Base case: one way to make 0 (empty combination)
    
    for coin in coins:
        for i in range(coin, amount + 1):
            # THE MAGIC: dp[i-c] contains combos summing to (i-c)
            # Adding current coin 'c' makes them sum to: (i-c) + c = i
            for combo in dp[i - coin]:
                new_combo = combo + [coin]
                dp[i].append(new_combo)
    
    return dp[amount]

# Test cases
print("=== DP COMBINATION TRACKING ===")
combinations = coinChangeCombinations(4, [1,2,3])
print(f"Amount=4, coins=[1,2,3]: {combinations}")
print(f"Count: {len(combinations)}")

combinations2 = coinChangeCombinations(7, [2,4])
print(f"Amount=7, coins=[2,4]: {combinations2}")
print(f"Count: {len(combinations2)}")

# Step-by-step demonstration
print("\n=== STEP-BY-STEP DEMONSTRATION ===")
print("Building combinations for amount=4, coins=[1,2,3]:")
print("Initial: dp[0]=[[]], dp[1..4]=[]")

# Simulate the process step by step
dp_demo = [[] for _ in range(5)]
dp_demo[0] = [[]]

for coin in [1, 2, 3]:
    print(f"\nProcessing coin {coin}:")
    for i in range(coin, 5):
        if dp_demo[i - coin]:
            new_combos = []
            for combo in dp_demo[i - coin]:
                new_combo = combo + [coin]
                new_combos.append(new_combo)
                print(f"  dp[{i}] gets {new_combo} (from dp[{i-coin}]={combo})")
            dp_demo[i].extend(new_combos)

print(f"\nFinal dp[4]: {dp_demo[4]}")

# Edge cases
print("\n=== EDGE CASES ===")
print(f"Amount=0: {coinChangeCombinations(0, [1,2,3])}")
print(f"Empty coins: {coinChangeCombinations(5, [])}")
print(f"Impossible amount: {coinChangeCombinations(3, [2,4])}")

'''
=== TIME AND SPACE COMPLEXITY ===
- Time Complexity: O(amount * num_coins * average_combinations_per_amount)
  The nested loops iterate amount * num_coins times
  Inside, we iterate over all combinations for dp[i-coin]

- Space Complexity: O(amount * average_combinations_per_amount)
  dp array stores combinations for each amount from 0 to target

=== KEY DIFFERENCES FROM COUNTING APPROACH ===
1. Instead of storing counts, we store actual combinations
2. dp[i] = [] becomes dp[i] = [[]] (empty combination for amount 0)
3. result[i] += result[i-coin] becomes: for each combo in dp[i-coin]: dp[i].append(combo + [coin])

=== WHEN TO USE THIS APPROACH ===
- When you need actual combinations, not just counts
- When amount is relatively small (to avoid memory explosion)
- When number of combinations is manageable

=== ALTERNATIVE FOR LARGE AMOUNTS ===
For very large amounts with many combinations, use backtracking approach
to generate combinations on-demand instead of storing all of them.
'''
