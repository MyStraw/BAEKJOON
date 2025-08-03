T = int(input())

for i in range(T):
    N = int(input())
    tri = list(range(N+3))
    tri[0] = tri[1] = tri[2] = 1    
    for j in range(N):
        tri[j+3] = tri[j] + tri[j+1]
    print(tri[N-1])