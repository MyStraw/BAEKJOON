import bisect
list = input().split()

N = int(list[0])
K = int(list[1])

fire = []
firelist = input().split()
for i in range(N):
    fire.append(int(firelist[i]))  

fire_sort = sorted(fire)

l = 0
r = bisect.bisect_left(fire_sort, K)
count = N-r
r-=1

while r > l:
    if fire_sort[l] + fire_sort[r] >=K:
        count +=1
        r -=1
    l += 1

if count>= 1:
    print(count)    
else:
    print(-1)