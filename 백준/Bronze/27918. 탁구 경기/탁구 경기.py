n = int(input())
rounds = [input().strip() for _ in range(n)]

score_d = 0 
score_p = 0  

for winner in rounds:
    if winner == 'D':
        score_d += 1
    else:  # 'P'
        score_p += 1

    if abs(score_d - score_p) >= 2:
        break

print(f"{score_d}:{score_p}")
