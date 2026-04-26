n, m = map(int, input().split())

board = []

for _ in range(n):
    board.append(list(map(int, input().split())))

tetrominoes = [
    [(0,0),(0,1),(0,2),(0,3)],
    [(0,0),(1,0),(2,0),(3,0)],

    [(0,0),(0,1),(1,0),(1,1)],

    [(0,0),(1,0),(2,0),(2,1)],
    [(0,1),(1,1),(2,1),(2,0)],
    [(0,0),(0,1),(1,0),(2,0)],
    [(0,0),(0,1),(1,1),(2,1)],
    [(0,0),(1,0),(1,1),(1,2)],
    [(0,2),(1,0),(1,1),(1,2)],
    [(0,0),(0,1),(0,2),(1,0)],
    [(0,0),(0,1),(0,2),(1,2)],

    [(0,0),(1,0),(1,1),(2,1)],
    [(0,1),(1,1),(1,0),(2,0)],
    [(0,1),(0,2),(1,0),(1,1)],
    [(0,0),(0,1),(1,1),(1,2)],

    [(0,0),(0,1),(0,2),(1,1)],
    [(0,1),(1,0),(1,1),(2,1)],
    [(0,1),(1,0),(1,1),(1,2)],
    [(0,0),(1,0),(1,1),(2,0)]
]

answer = 0

for i in range(n):
    for j in range(m):
        for shape in tetrominoes:
            total = 0
            possible = True

            for dx, dy in shape:
                x = i + dx
                y = j + dy

                if x < 0 or x >= n or y < 0 or y >= m:
                    possible = False
                    break

                total += board[x][y]

            if possible and total > answer:
                answer = total

print(answer)