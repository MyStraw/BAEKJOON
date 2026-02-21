T = int(input())
out = []

for _ in range(T):
    m1 = int(input())
    e1 = set()
    for _ in range(m1):
        u, v = map(int, input().split())
        if u > v:
            u, v = v, u
        e1.add((u, v))

    m2 = int(input())
    e2 = set()
    for _ in range(m2):
        u, v = map(int, input().split())
        if u > v:
            u, v = v, u
        e2.add((u, v))

    if len(e1) != len(e2):
        out.append("no")
        continue

    found = False
    for p in [(1,2,3),(1,3,2),(2,1,3),(2,3,1),(3,1,2),(3,2,1)]:
        mapped = set()
        for u, v in e1:
            mu = p[u-1]
            mv = p[v-1]
            if mu > mv:
                mu, mv = mv, mu
            mapped.add((mu, mv))
        if mapped == e2:
            found = True
            break

    out.append("yes" if found else "no")

print("\n".join(out))