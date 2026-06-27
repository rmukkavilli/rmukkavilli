from collections import deque

def number_of_islands(grid):
    directions = [(-1,0), (1,0), (0,-1),(0,1)]
    queue = []
    islands = 0
    
    def bfs(r,c, grid, rows, cols, directions):     
        queue = deque([(r,c)])
        grid[r][c] = 0

        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                new_row = row + dr
                new_col= col + dc
                print(new_row, ",",  new_col)
                if (0 < new_row < rows and 0 < new_col < cols and grid[r][c] == 1):
                     grid[r][c] == 0
                     queue.append(new_row, new_col)
                

    
    rows=len(grid)
    cols=len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                islands +=1
                bfs(r, c, grid, rows, cols, directions)    
    print(grid)
    return islands


grid = [[1, 1, 0],[1, 0, 0],[0, 0, 1]]
print(number_of_islands(grid))