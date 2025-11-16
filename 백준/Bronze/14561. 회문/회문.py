def to_base(n, base):
    digits = "0123456789ABCDEF"
    res = ""
    while n > 0:
        res += digits[n % base]
        n //= base
    return res[::-1]

T = int(input())
for _ in range(T):
    A, n = map(int, input().split())
    s = to_base(A, n)
    print(1 if s == s[::-1] else 0)
