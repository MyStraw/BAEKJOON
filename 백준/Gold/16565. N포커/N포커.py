from math import comb

def fourCard(N):
    mod = 10007
    total = 0    
    set = N // 4
    
    for i in range(1, set + 1):
        jungbok = comb(13, i) * comb(52 - 4*i, N - 4*i)
        if i % 2 == 1:
            total += jungbok
        else:
            total -= jungbok
    
    return total % mod

N = int(input())
print(fourCard(N))