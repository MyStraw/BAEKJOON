import sys
input = sys.stdin.readline

while True:
    input_str = input().split()
    if not input_str:
        break
    N = int(input_str[0])
    M = int(input_str[1])
    if N == 0 and M == 0:
        break

    sang = set()
    for i in range(N):
        sang.add(int(input()))

    cnt = 0
    for j in range(M):
        if int(input()) in sang:
            cnt += 1

    print(cnt)
