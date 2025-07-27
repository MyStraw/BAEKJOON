n, m = map(int, input().split())

L = m + 14 - n
x = m + 7

if x > L:
  print(x - L)
else:
  print(x)