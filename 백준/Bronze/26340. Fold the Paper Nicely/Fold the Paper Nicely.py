import sys

def solve():
    n = int(sys.stdin.readline())
    for _ in range(n):
        s1, s2, folds = map(int, sys.stdin.readline().split())
        
        print(f"Data set: {s1} {s2} {folds}")
        
        temp_s1, temp_s2 = s1, s2
        
        for _ in range(folds):
            if temp_s1 >= temp_s2:
                temp_s1 //= 2
            else:
                temp_s2 //= 2
        
        if temp_s1 >= temp_s2:
            print(temp_s1, temp_s2)
        else:
            print(temp_s2, temp_s1)
            
        print()

solve()