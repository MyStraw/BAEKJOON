w_c, h_c, w_s, h_s = map(int, input().split())
print(1 if w_s + 2 <= w_c and h_s + 2 <= h_c else 0)