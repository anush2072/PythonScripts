'''
There is an m x n grid where you are allowed to move either down or to the right at any point in time.

Given the two integers m and n, return the number of possible unique paths that can be taken 
from the top-left corner of the grid (grid[0][0]) to the bottom-right corner (grid[m - 1][n - 1]).
'''
import numpy as np

def uniquePaths(m: int, n: int) -> int:
    grid = np.zeros((m+1,n+1), dtype=int)
    grid[m-1][n-1] = 1

    for i in range(m-1,-1,-1):
        for j in range(n-1,-1,-1):
            grid[i][j] = grid[i][j]+(grid[i+1][j]+grid[i][j+1])
    
    return int(grid[0][0])

print(uniquePaths(m = 3, n = 6))
print(uniquePaths(m = 3, n = 3))

'''
=== TIME AND SPACE COMPLEXITY ===
- Time Complexity: O(m * n)
  We visit each cell in the (m x n) grid exactly once
  
- Space Complexity: O(m * n)
  DP grid of size (m+1) x (n+1) to store intermediate results
  Can be optimized to O(n) using 1D DP array

=== INTERVIEW FOLLOWUP QUESTIONS ===

1. **Space Optimization**: "Can you optimize space from O(m*n) to O(n)?"
   - Use 1D DP array: dp[j] = dp[j] + dp[j+1]
   - Only need previous row values, not entire grid

2. **Mathematical Approach**: "Is there a formula-based solution?"
   - Yes: C(m+n-2, m-1) = (m+n-2)! / ((m-1)! * (n-1)!)
   - Use combinatorics: choose (m-1) down moves from (m+n-2) total moves

3. **Obstacles**: "What if some cells have obstacles?"
   - Set grid[i][j] = 0 for obstacle cells
   - Skip obstacle cells in DP calculation

4. **Different Moves**: "What if you can also move diagonally?"
   - DP recurrence: grid[i][j] = grid[i+1][j] + grid[i][j+1] + grid[i+1][j+1]

5. **Large Grids**: "How to handle very large m, n values?"
   - Use combinatorial formula with modular arithmetic
   - Use DP with space optimization

=== REAL-TIME APPLICATIONS ===

1. **Robot Navigation**: Path planning for robots in warehouses
   - Amazon warehouse robots finding optimal routes
   - Manufacturing robots moving on grid floors

2. **Network Routing**: Finding paths in grid-based network topologies
   - Data packet routing in mesh networks
   - Circuit board trace routing

3. **Game Development**: Character movement in grid-based games
   - Puzzle games with grid movement
   - Strategy games with unit pathfinding

4. **Urban Planning**: Traffic flow analysis on grid-like street networks
   - Optimizing traffic light sequences
   - Emergency vehicle route planning

5. **Image Processing**: Pixel traversal in computer vision
   - Flood fill algorithms
   - Connected component analysis

6. **DNA Sequencing**: Path finding in sequence alignment grids
   - Bioinformatics algorithms
   - Protein structure analysis
'''