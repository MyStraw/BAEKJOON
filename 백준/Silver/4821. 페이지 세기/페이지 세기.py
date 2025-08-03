while True:    
    N = int(input())
    if N == 0:
        break
    line = input().split(",")
    contain = set()
    for pages in line:
        page = pages.split("-")     
        if len(page) == 1:
            low = high = int(page[0])
        elif len(page) == 2:
            low = int(page[0])
            high = int(page[1])       
        else:
            continue
        
        if low > high:
            continue
        if low > N:
            continue
        if high > N:
            high = N
        contain.update(i for i in range(low, high+1, 1))
    print(len(contain))