n = int(input())
difficulties = [int(input()) for _ in range(n)]

first = difficulties[0]
if first == min(difficulties):
    print("ez")
elif first == max(difficulties):
    print("hard")
else:
    print("?")
