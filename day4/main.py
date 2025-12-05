import sys
from typing import List, Tuple



def main():
    G = sys.stdin.readlines()
    grid = []
    for i, v in enumerate(G):
        v = v.strip()
        grid.append([c for c in v])


    def valid(nx, ny):
        return nx >= 0 and nx < N and ny >= 0 and ny < M and grid[nx][ny] == '@'
    
    N, M = len(grid), len(grid[0])
    ret = 0
    def go(grid):
        res = []
        for x in range(N):
            for y in range(M):
                if grid[x][y] != '@':
                    continue
                cnt = 0
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if dx == 0 and dy == 0:
                            continue
                        else:
                            nx, ny = x + dx, y + dy
                            if valid(nx, ny):
                                cnt += 1
                if cnt < 4:
                    grid[x][y] = '.'
                    res.append((x, y))
        return (grid, res)
            
    prev_grid = grid
    while True:
        ng, ret1 = go(grid)
        if not ret1:
            break
        ret += len(ret1)
        prev_grid, ng = ng, prev_grid
    print(ret) 


if __name__ == "__main__":
    main()