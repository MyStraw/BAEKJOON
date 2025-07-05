while True:
    n = int(input())
    if n == 0:
        break
    a = list(map(int, input().split()))
    max_members = 0
    for i in range(n):        
        current_sum = 0
        for j in range(3):
            if i - j >= 0:
                current_sum += a[i - j]
        if current_sum > max_members:
            max_members = current_sum
    print(max_members)
