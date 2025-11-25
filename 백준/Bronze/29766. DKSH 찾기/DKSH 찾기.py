s = input()
target = "DKSH"
n = len(s)
cnt = 0

for i in range(n - 3):
    if s[i:i+4] == target:
        cnt += 1

print(cnt)
