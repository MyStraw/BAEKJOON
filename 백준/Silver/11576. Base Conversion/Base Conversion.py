A, B = map(int, input().split())
m = int(input())
digits = list(map(int, input().split()))

value = 0
for d in digits:
    value = value * A + d

result = []
while value > 0:
    result.append(value % B)
    value //= B

print(' '.join(map(str, reversed(result))))
