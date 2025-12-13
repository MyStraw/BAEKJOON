import sys

p, r = map(int, sys.stdin.readline().split())

v = p / r

if v < 0.2:
    print("weak")
elif v < 0.4:
    print("normal")
elif v < 0.6:
    print("strong")
else:
    print("very strong")
