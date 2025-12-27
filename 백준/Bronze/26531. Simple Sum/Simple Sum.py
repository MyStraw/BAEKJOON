import sys

s = sys.stdin.readline().strip()
a = int(s[0])
b = int(s[4])
c = int(s[8])

print("YES" if a + b == c else "NO")
