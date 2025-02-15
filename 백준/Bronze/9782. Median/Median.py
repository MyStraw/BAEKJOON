import sys

case_number = 1

for line in sys.stdin:
    data = list(map(int, line.split()))
    if data[0] == 0:
        break
    n, values = data[0], data[1:]
    mid = n // 2
    if n % 2 == 1:
        median = values[mid]
    else:
        median = (values[mid - 1] + values[mid]) / 2
    print(f"Case {case_number}: {median:.1f}")
    case_number += 1