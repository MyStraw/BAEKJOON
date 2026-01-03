import sys

input = sys.stdin.readline

input().strip()
input().strip()
input().strip()

out = []
for A in range(1, 11):
    for B in range(1, 11):
        for C in range(1, 11):
            for D in range(1, 11):
                w = A * 1000 + B - D * 1000
                if w < 0:
                    out.append("-1")
                else:
                    out.append(str(w))

sys.stdout.write("\n".join(out))
