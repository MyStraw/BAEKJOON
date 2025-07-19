N = int(input())
tang = list(map(int, input().split()))

max_len = 0
count = {} #defaultdict(int) 이런게 있다 파이썬엔
left = 0

for right in range(N):
    fruit = tang[right]
    if fruit in count:
        count[fruit] +=1
    else:
        count[fruit] = 1 #없으면 1개 넣기
        
    while len(count) >2:
        left_fruit = tang[left]
        count[left_fruit] -=1 #2개 넘으면 왼쪽 슬라이드 이동
        if count[left_fruit] == 0:
            del count[left_fruit] #익셔너리에서 해당 키 항목 삭제
        left +=1


    max_len = max(max_len, right - left +1)
print(max_len)