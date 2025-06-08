T = int(input())
for _ in range(T):
    s = input().strip()
    count_a = s.count('a')
    count_b = s.count('b')
    print(min(count_a, count_b))
