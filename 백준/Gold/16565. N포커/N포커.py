import math

def fourCard(N):
    MOD = 10007

    if N < 4:
        return 0
    elif 4 <= N < 8:       
        return (13 * math.comb(48, N - 4)) % MOD
    elif 8 <= N < 12:        
        return (13 * math.comb(48, N - 4) - math.comb(13, 2) * math.comb(44, N - 8)) % MOD
    elif 12 <= N < 16:        
        return (13 * math.comb(48, N - 4) - math.comb(13, 2) * math.comb(44, N - 8) + math.comb(13, 3) * math.comb(40, N - 12)) % MOD
    elif 16 <= N < 20:        
        return (13 * math.comb(48, N - 4) - math.comb(13, 2) * math.comb(44, N - 8) + math.comb(13, 3) * math.comb(40, N - 12) - math.comb(13, 4) * math.comb(36, N - 16)) % MOD
    elif 20 <= N < 24:        
        return (13 * math.comb(48, N - 4) - math.comb(13, 2) * math.comb(44, N - 8) + math.comb(13, 3) * math.comb(40, N - 12) - math.comb(13, 4) * math.comb(36, N - 16) + math.comb(13, 5) * math.comb(32, N - 20)) % MOD
    elif 24 <= N < 28:        
        return (13 * math.comb(48, N - 4) - math.comb(13, 2) * math.comb(44, N - 8) + math.comb(13, 3) * math.comb(40, N - 12) - math.comb(13, 4) * math.comb(36, N - 16) + math.comb(13, 5) * math.comb(32, N - 20) - math.comb(13, 6) * math.comb(28, N - 24)) % MOD
    elif 28 <= N < 32:        
        return (13 * math.comb(48, N - 4) - math.comb(13, 2) * math.comb(44, N - 8) + math.comb(13, 3) * math.comb(40, N - 12) - math.comb(13, 4) * math.comb(36, N - 16) + math.comb(13, 5) * math.comb(32, N - 20) - math.comb(13, 6) * math.comb(28, N - 24) + math.comb(13, 7) * math.comb(24, N - 28)) % MOD
    elif 32 <= N < 36:        
        return (13 * math.comb(48, N - 4) - math.comb(13, 2) * math.comb(44, N - 8) + math.comb(13, 3) * math.comb(40, N - 12) - math.comb(13, 4) * math.comb(36, N - 16) + math.comb(13, 5) * math.comb(32, N - 20) - math.comb(13, 6) * math.comb(28, N - 24) + math.comb(13, 7) * math.comb(24, N - 28) - math.comb(13, 8) * math.comb(20, N - 32)) % MOD
    elif 36 <= N < 40:        
        return (13 * math.comb(48, N - 4) - math.comb(13, 2) * math.comb(44, N - 8) + math.comb(13, 3) * math.comb(40, N - 12) - math.comb(13, 4) * math.comb(36, N - 16) + math.comb(13, 5) * math.comb(32, N - 20) - math.comb(13, 6) * math.comb(28, N - 24) + math.comb(13, 7) * math.comb(24, N - 28) - math.comb(13, 8) * math.comb(20, N - 32) + math.comb(13, 9) * math.comb(16, N - 36)) % MOD
    else:       
        return math.comb(52, 52 - N) % MOD

N = int(input())
print(fourCard(N))
