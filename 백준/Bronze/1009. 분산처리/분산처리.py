T = int(input())

for i in range(T):
    test = input().split()
    first = int(test[0])
    last = int(test[1])     
    num = pow(first, last,10) 
  
    if num != 0:
        print(num)
    elif num == 0:
        print(10)