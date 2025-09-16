N = int(input())
F = int(input())

base = (N // 100)*100
rem = base % F
if rem ==0:  
    result = base
else:
    result = base + (F -rem)

print(f"{result % 100:02d}")
