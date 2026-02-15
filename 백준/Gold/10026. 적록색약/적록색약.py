N = int(input())
grid = [input().strip() for _ in range(N)]

visited = [[0] * N for _ in range(N)]
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

cnt1 = 0
for i in range(N):
    for j in range(N):
        if visited[i][j]:
            continue
        cnt1 += 1
        color = grid[i][j]
        q = [(i, j)]
        visited[i][j] = 1
        head = 0
        while head < len(q):
            x, y = q[head]
            head += 1
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and grid[nx][ny] == color:
                    visited[nx][ny] = 1
                    q.append((nx, ny))

visited2 = [[0] * N for _ in range(N)]

def same_rg(a, b):
    if a == b:
        return True
    if a == 'B' or b == 'B':
        return False
    return True

cnt2 = 0
for i in range(N):
    for j in range(N):
        if visited2[i][j]:
            continue
        cnt2 += 1
        q = [(i, j)]
        visited2[i][j] = 1
        head = 0
        while head < len(q):
            x, y = q[head]
            head += 1
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N and not visited2[nx][ny] and same_rg(grid[x][y], grid[nx][ny]):
                    visited2[nx][ny] = 1
                    q.append((nx, ny))

print(cnt1, cnt2)