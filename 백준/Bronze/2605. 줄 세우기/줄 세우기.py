n = int(input())
nums = list(map(int, input().split()))

line = []

for i in range(n):
    pick = nums[i]
    student = i + 1  # 1번부터
    line.insert(len(line) - pick, student)

print(' '.join(map(str, line)))
