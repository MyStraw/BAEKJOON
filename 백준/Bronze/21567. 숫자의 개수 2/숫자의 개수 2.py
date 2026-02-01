A = int(input())
B = int(input())
C = int(input())

result = str(A * B * C)

count = [0] * 10

for ch in result:
    count[int(ch)] += 1

for i in range(10):
    print(count[i])
