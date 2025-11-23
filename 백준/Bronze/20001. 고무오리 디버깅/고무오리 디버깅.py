input()
cnt = 0
while True:
    s = input()
    if s == "고무오리 디버깅 끝":
        break
    if s == "문제":
        cnt += 1
    else:
        if cnt > 0:
            cnt -= 1
        else:
            cnt += 2
print("고무오리야 사랑해" if cnt == 0 else "힝구")
