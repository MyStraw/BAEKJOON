n, u, l = map(int, input().split())
baekjoon_ok = n >= 1000
maple_ok = (u >= 8000) or (l >= 260)
print("Very Good" if baekjoon_ok and maple_ok else "Good" if baekjoon_ok else "Bad")
