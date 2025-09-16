from collections import Counter

N = int(input())
participants = [input().strip() for _ in range(N)]
finishers = [input().strip() for _ in range(N-1)]

counter = Counter(participants)
for f in finishers:
    counter[f] -= 1

for name, cnt in counter.items():
    if cnt > 0:
        print(name)
        break
