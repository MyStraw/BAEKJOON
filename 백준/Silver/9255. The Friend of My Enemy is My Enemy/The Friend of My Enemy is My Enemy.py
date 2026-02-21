K = int(input())
out = []

for ds in range(1, K + 1):
    n, m = map(int, input().split())
    adj = [set() for _ in range(n + 1)]

    for _ in range(m):
        a, b = map(int, input().split())
        adj[a].add(b)
        adj[b].add(a)

    s = int(input())

    friends = sorted(adj[s])

    out.append(f"Data Set {ds}:")
    if friends:
        out.append(" ".join(map(str, friends)))
    else:
        out.append("")
    out.append("")

print("\n".join(out))