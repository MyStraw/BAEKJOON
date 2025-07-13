total_time = 0
for _ in range(4):
    total_time += int(input())

total_time += 300

if total_time <= 1800:
    print("Yes")
else:
    print("No")
