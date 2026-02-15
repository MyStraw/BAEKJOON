out = []

while True:
    try:
        line = input().strip()
    except EOFError:
        break

    if line == "0":
        break
    if line == "":
        continue

    t = list(map(int, line.split()))
    a = t[0]

    leaves = 1
    idx = 1
    for _ in range(a):
        s = t[idx]
        p = t[idx + 1]
        leaves = leaves * s - p
        idx += 2

    out.append(str(leaves))

print("\n".join(out))