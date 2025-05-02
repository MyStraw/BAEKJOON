k, w, m = map(int, input().split())
print(max(0, (w - k + m - 1) // m))
