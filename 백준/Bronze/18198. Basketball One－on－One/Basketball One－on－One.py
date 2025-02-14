record = input().strip()
score_A = 0
score_B = 0
for i in range(0, len(record), 2):
    if record[i] == 'A':
        score_A += int(record[i+1])
    else:
        score_B += int(record[i+1])
    if score_A >= 11 or score_B >= 11:
        if score_A >= 10 and score_B >= 10:
            if abs(score_A - score_B) >= 2:
                break
        else:
            break
print('A' if score_A > score_B else 'B')