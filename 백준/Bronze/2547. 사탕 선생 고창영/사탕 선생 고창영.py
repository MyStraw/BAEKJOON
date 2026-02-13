T = int(input())
out = []

for _ in range(T):
    line = input().strip()
    while line == "":
        line = input().strip()

    N = int(line)
    s = 0
    for _ in range(N):
        s = (s + int(input().strip())) % N

    out.append("YES" if s % N == 0 else "NO")

print("\n".join(out))