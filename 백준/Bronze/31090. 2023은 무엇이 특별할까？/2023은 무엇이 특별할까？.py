import sys

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    last = n % 100
    if (n + 1) % last == 0:
        print("Good")
    else:
        print("Bye")
