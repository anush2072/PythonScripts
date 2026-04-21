'''
You are given a matrix grid where grid[i] is either a 0 (representing water) or 1 (representing land).

An island is defined as a group of 1's connected horizontally or vertically. 
You may assume all four edges of the grid are surrounded by water.

Return the maximum perimeter of an island in grid. If no island exists, return 0.
'''
from typing import List
from collections import deque

def maxPerimeterOfIsland(grid: List[List[int]]) -> int:
    if not grid:
        return 0
    
    ROWS, COLS = len(grid), len(grid[0])
    directions = [[1,0], [-1,0], [0,1], [0,-1]]
    max_perimeter = 0

    def bfs(r,c):
        q = deque([(r,c)])
        visited = set([(r,c)])
        perimeter = 0
        
        while q:
            row, col = q.popleft()
            for dr, dc in directions:
                nr, nc = row+dr, col+dc
                # Out of bounds or water = exposed edge
                if nr<0 or nr>=ROWS or nc<0 or nc>=COLS or grid[nr][nc] == 0:
                    perimeter += 1
                elif (nr,nc) not in visited:  # Unvisited land
                    q.append((nr,nc))
                    visited.add((nr,nc))
        
        return perimeter

    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 1:
                perimeter = bfs(r,c)
                max_perimeter = max(max_perimeter, perimeter)

    return max_perimeter

# Test cases
print(maxPerimeterOfIsland([[1,1,0,0],[1,0,0,0],[1,1,1,0],[0,0,1,1]]))
print(maxPerimeterOfIsland([[1,0]]))
print(maxPerimeterOfIsland([[0,0,0],[0,0,0]]))

'''
=== PERIMETER CALCULATION EXPLANATION ===

For the test case:
[[1,1,0,0],
 [1,0,0,0], 
 [1,1,1,0],
 [0,0,1,1]]

Expected perimeter = 18

Manual count:
- Each cell contributes 4 edges initially
- Subtract 1 for each shared edge with adjacent land
- Total = 18

=== KEY FIX ===
Using visited set instead of modifying grid prevents:
1. Double-counting shared edges
2. Incorrect boundary checks due to grid modification
3. Cross-island interference

=== TIME AND SPACE COMPLEXITY ===
- Time: O(ROWS * COLS) - each cell visited once
- Space: O(ROWS * COLS) - visited set in worst case
'''