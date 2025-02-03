from collections import deque

def solve():
    N, M, K = map(int, input().split())
    grid = [[0] * M for _ in range(N)]
    for _ in range(K):
        r, c = map(int, input().split())
        grid[r-1][c-1] = 1
    max_food = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    def bfs(i, j):
        queue = deque()
        queue.append((i, j))
        grid[i][j] = 0
        count = 1
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == 1:
                    grid[nx][ny] = 0
                    queue.append((nx, ny))
                    count += 1
        return count
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1:
                max_food = max(max_food, bfs(i, j))
    print(max_food)

if __name__ == "__main__":
    solve()