'''
You are given a matrix grid where grid[i] is either a 0 (representing water) or 1 (representing land).

An island is defined as a group of 1's connected horizontally or vertically. 
You may assume all four edges of the grid are surrounded by water.

The area of an island is defined as the number of cells within the island.

Return the maximum area of an island in grid. If no island exists, return 0.
'''
from typing import List
from collections import deque

def maxAreaOfIsland(grid: List[List[int]]) -> int:
    if not grid:
        return 0
    
    ROWS, COLS = len(grid), len(grid[0])
    directions = [[1,0], [-1,0], [0,1], [0,-1]]
    max_area = 0

    def bfs(r,c):
        q = deque()
        q.append((r,c))
        grid[r][c] = 0
        area = 1
        while q:
            row, col = q.popleft()
            for dr, dc in directions:
                nr, nc = row+dr, col+dc
                if nr<0 or nr>=ROWS or nc<0 or nc>=COLS or grid[nr][nc] == 0:
                    continue
                q.append((nr,nc))
                grid[nr][nc] = 0
                area += 1
        return area

    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 1:
                area = bfs(r,c)
                max_area = max(max_area, area)

    return max_area

print(maxAreaOfIsland(grid=[[0,1,1,0,1],[1,0,1,0,1],[0,1,1,0,1],[0,1,0,0,1]]))