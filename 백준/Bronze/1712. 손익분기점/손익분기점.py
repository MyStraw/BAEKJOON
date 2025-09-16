A, B, C = map(int, input().split())
if C <= B:
    print(-1)
else:   
    break_even_point = (A // (C - B)) + 1
    print(break_even_point)