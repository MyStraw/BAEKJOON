n = int(input())
m = int(input())
s = input()

answer = 0
count =0
i = 1

while i < m - 1:
    if s[i -1] == "I" and s[i] == "O" and s[i +1] == "I":
        count += 1

        if count == n:
            answer += 1
            count -= 1

        i +=2
    else:
        count = 0
        i += 1

print(answer)