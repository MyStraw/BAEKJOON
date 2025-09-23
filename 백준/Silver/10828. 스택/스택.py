import sys

input = sys.stdin.readline
N = int(input())

stack = []
for i in range(N):
    line = input().split()
    cmd = line[0]
    if len(line) == 2:
        num = int(line[1])
            
    if cmd == "push":
        stack.append(num)
    elif cmd == "top":
        if len(stack) !=0:
            print(stack[-1])
        else:
            print(-1)
    elif cmd == "size":
        print(len(stack))
    elif cmd == "empty":
        print(1 if len(stack) == 0 else 0)
    elif cmd == "pop":
        if len(stack) !=0:
            print(stack.pop())
        else:
            print(-1)