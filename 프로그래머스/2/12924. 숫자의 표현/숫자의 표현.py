def solution(n):
    loop = 0
    for i in range(1,n+1):
        result = 0
        j = i
        while result <= n:
            result +=j
            j+=1
            if result ==n:
                loop +=1
                break
    return loop
