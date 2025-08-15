θ1, θ2 = map(int, input().split())
ok = (θ2 % 6 == 0) and ((θ2 // 6 - 2 * θ1) % 60 == 0)
print("O" if ok else "X")
