T = int(input())

for _ in range(T):
    p = int(input())
    
    max_price = -1
    answer = ""
    
    for _ in range(p):
        c, name = input().split()
        c = int(c)
        
        if c > max_price:
            max_price = c
            answer = name
    
    print(answer)