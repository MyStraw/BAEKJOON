N = input()

counts = [0] * 10

for i in N:
    digit = int(i)
    counts[digit] += 1
six_nine = counts[6] + counts[9]
counts[6] = (six_nine + 1) // 2  
counts[9] = 0
print(max(counts))
