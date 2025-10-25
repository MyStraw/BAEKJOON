T = int(input())
for _ in range(T):
    K = int(input())
    students = list(map(int, input().split()))
    N = int(input())
    records = {}
    for _ in range(N):
        num, h, m = map(int, input().split())
        if num in students and h != -1 and (h < 6 or (h == 6 and m == 0)):
            total_min = h * 60 + m
            if num not in records:
                records[num] = total_min
    best_student = min(records.items(), key=lambda x: x[1])[0]
    print(best_student, len(records))
