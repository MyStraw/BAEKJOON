def count_good_intervals(L, S, n):
    S_sorted = sorted(S)
    if n in S_sorted:
        return 0
    
    left = 0
    right = 0
    
    for i in range(L):
        if S_sorted[i] < n:
            left = S_sorted[i]
        else:
            right = S_sorted[i]
            break
    
    if left == 0:
        left = 0
    if right == 0:
        right = S_sorted[-1] + 1
    
    A_min = left + 1
    A_max = n
    B_min = n
    B_max = right - 1
    
    count = 0
    for A in range(A_min, A_max + 1):
        for B in range(B_min, B_max + 1):
            if A < B:
                count += 1
    
    return count

L = int(input())
S = list(map(int, input().split()))
n = int(input())

print(count_good_intervals(L, S, n))