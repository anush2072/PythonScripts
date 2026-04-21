'''
Given a 2D grid grid where '1' represents land and '0' represents water, count and return the number of islands.

An island is formed by connecting adjacent lands horizontally or vertically and is surrounded by water. 
You may assume water is surrounding the grid (i.e., all the edges are water).
'''
from typing import List
from collections import deque

def numIslands(grid: List[List[str]]) -> int:
    if not grid:
        return 0
    ROWS, COLS = len(grid), len(grid[0])
    directions = [[1,0], [-1,0], [0,1], [0,-1]]
    islands = 0

    def bfs(r,c):
        q = deque()
        q.append((r,c))
        grid[r][c] = "0"

        while q:
            row, col = q.popleft()
            for dr, dc in directions:
                nr, nc = row+dr, col+dc
                if (nr<0 or nc<0 or nr>=ROWS or nc>=COLS or grid[nr][nc]=="0"):
                    continue
                q.append((nr,nc))
                grid[nr][nc] = "0"


    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == "1":
                bfs(r,c)
                islands = islands+1
    
    return islands

print(numIslands(grid=[["0","1","1","1","0"],["0","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))
print(numIslands(grid=[["1","1","0","0","1"],["1","1","0","0","1"],["0","0","1","0","0"],["0","0","0","1","1"]]))