t = int(input())

for _ in range(t):
    x = int(input())
    arr = input().split()

    total = 0
    is_many = False

    for i in range(0, 2 * x + 1, 2):
        if arr[i] == "!":
            is_many = True
            break
        total += int(arr[i])
        if total > 9:
            is_many = True
            break

    if is_many:
        print("!")
    else:
        print(total)