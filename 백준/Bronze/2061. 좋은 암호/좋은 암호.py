k_str, l_str = input().split()
K = int(k_str)
L = int(l_str)

n = L - 1
if n < 2:
    print("GOOD")
else:
    is_prime = bytearray(b"\x01") * (n + 1)
    is_prime[0] = 0
    is_prime[1] = 0

    i = 2
    while i * i <= n:
        if is_prime[i]:
            j = i * i
            step = i
            while j <= n:
                is_prime[j] = 0
                j += step
        i += 1

    p = 2
    while p <= n:
        if is_prime[p]:
            if K % p == 0:
                print("BAD", p)
                break
        p += 1
    else:
        print("GOOD")