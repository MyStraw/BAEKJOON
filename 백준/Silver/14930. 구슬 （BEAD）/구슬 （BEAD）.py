def simulate(N, t, balls):
    red = balls[0]
    balls.sort()
    idx = balls.index(red)
    
    vPos = [x + v * t for x, v in balls]
    vPos.sort()
    
    return vPos[idx]

N, t = map(int, input().split())
balls = [list(map(int, input().split())) for _ in range(N)]
print(simulate(N, t, balls))