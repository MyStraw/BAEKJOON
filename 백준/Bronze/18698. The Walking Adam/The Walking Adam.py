T = int(input())

for _ in range(T):
    steps = input()
    count = 0
    for step in steps:
        if step == 'D':
            break
        count += 1
    print(count)