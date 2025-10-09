N, M = map(int, input().split())
total_minutes = (M * 24 * 60) // N
if total_minutes == 24 * 60:
    print("24:00")
else:
    h = total_minutes // 60
    m = total_minutes % 60
    print(f"{h:02d}:{m:02d}")