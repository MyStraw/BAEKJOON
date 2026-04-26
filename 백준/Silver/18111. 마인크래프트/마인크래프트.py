n, m, b = map(int, input().split())

count = [0]* 257

for _ in range(n):
    row = list(map(int, input().split()))
    for h in row:
        count[h] += 1

answer_time = 1000000000000
answer_height = 0

for target in range(257):
    remove = 0
    add = 0

    for h in range(257):
        if h > target:
            remove += (h -target) *count[h]
        else:
            add += (target -h) *count[h]

    if remove + b >= add:
        time = remove * 2+add

        if time < answer_time or (time == answer_time and target >answer_height):
            answer_time = time
            answer_height =target

print(answer_time, answer_height)