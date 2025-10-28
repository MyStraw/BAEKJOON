nums = [int(input()) for _ in range(7)]
odds = [n for n in nums if n % 2 == 1]

if not odds:
    print(-1)
else:
    print(sum(odds))
    print(min(odds))
