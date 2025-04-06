n, k, a, b = map(int, input().split())
lift_time = abs(k - 1) * b + (n - 1) * b
stairs_time = (n - 1) * a
print(lift_time, stairs_time)