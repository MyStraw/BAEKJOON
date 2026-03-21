a, b = map(int, input().split())

if a > b:
    a, b = b, a

start = a + 1
end = b - 1

if start > end:
    print(0)
else:
    nums = list(range(start, end + 1))
    print(len(nums))
    print(*nums)