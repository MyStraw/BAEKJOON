import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    s, p = input().split()
    n, m = len(s), len(p)
    
    i = 0
    time = 0
    while i < n:
        if i + m <= n and s[i:i+m] == p:
            time += 1
            i += m
        else:
            time += 1
            i += 1
    print(time)
