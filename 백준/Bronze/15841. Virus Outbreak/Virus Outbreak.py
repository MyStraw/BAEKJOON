fib = [0] * 491
fib[1] = 1
fib[2] = 1

for i in range(3, 491):
    fib[i] = fib[i - 1] + fib[i - 2]

while True:
    try:
        x = int(input())
    except:
        break
    if x == -1:
        break
    print(f"Hour {x}: {fib[x]} cow(s) affected")