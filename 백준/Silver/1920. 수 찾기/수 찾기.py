N = int(input())

line = list(map(int,input().split()))

M = int(input())

contain = list(map(int,input().split()))

line.sort()

one = False
for c in contain:
    first = 0
    end = N-1
    while first<=end:
        mid = (first + end)//2
        
        if line[mid] > c:
            end = mid-1
        elif line[mid] < c:
            first =  mid + 1
        elif line[mid] == c:
            one = True
            break
        one = False
        
    if one:
        print(1)
    else:
        print(0)



    
