def main():
    N = int(input())
    records = []
    for _ in range(N):
        S, W, D, P = input().split()
        W = int(W)
        D = int(D)
        P = int(P)
        records.append((S, W, D, P))
    
    money = {}
    for _ in range(N):
        S, M = input().split()
        M = int(M)
        money[S] = M
    
    day = [False] * 80
    for record in records:
        S, W, D, P = record
        if P <= money[S]:  
            day[W * 7 + D] = True  
    
    max_days = 0
    current_days = 0
    for i in range(80):
        if day[i]:
            current_days += 1
            if current_days > max_days:
                max_days = current_days
        else:
            current_days = 0
    
    print(max_days)

if __name__ == "__main__":
    main()