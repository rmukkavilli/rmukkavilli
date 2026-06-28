from collections import deque

def rotten_oranges(grid):
    directions = [(-1,0), (1,0), (0,-1),(0,1)]
    queue = []
    fresh = 0
    minutes = 0
    
    def bfs(r,c, grid, rows, cols, directions, fresh, minutes): 
        while queue and fresh > 0:
            row, col = queue.popleft()
            for dr, dc in directions:
                new_dr = row +dr
                new_dc = col+dc
            if (0< new_dr < rows and o < new_col < dc and grid[new_dr][new_dc] == 1):
                grid[new_dr][new_dc] = 2
                fresh -=1
                queue.append((new_dr, new_dc))
        minutes +=1

       

    
    rows=len(grid)
    cols=len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r,c))
            elif grid[r][c] ==1:
                fresh +1
                bfs(r, c, grid, rows, cols, directions, fresh, minutes)    
    print(grid)
    return minutes if fresh == 0 else 1


grid = [[2, 1, 1],[1, 1, 0],[0, 1, 1]]
print(rotten_oranges(grid))