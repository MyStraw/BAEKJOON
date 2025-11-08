votes = list(map(int, input().split()))
tier16 = votes[0]
count = 0
for v in votes[1:]:
    if tier16 - v <= 1000:
        count += 1
print(count)
