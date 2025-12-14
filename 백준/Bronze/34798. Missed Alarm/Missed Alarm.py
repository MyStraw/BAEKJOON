import sys

a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()

ah, am = map(int, a.split(":"))
bh, bm = map(int, b.split(":"))

if (bh, bm) > (ah, am):
    print("YES")
else:
    print("NO")
