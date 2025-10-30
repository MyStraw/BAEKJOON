A, B = map(int, input().split())
C, D = map(int, input().split())

tables = [
    (A, B, C, D),     
    (C, A, D, B),       
    (D, C, B, A),      
    (B, D, A, C)        
]

max_value = -1
answer = 0

for i in range(4):
    a, b, c, d = tables[i]
    value = a / c + b / d
    if value > max_value:
        max_value = value
        answer = i

print(answer)
