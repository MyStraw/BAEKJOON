K = int(input())
out = []

for ds in range(1, K + 1):
    n, W, E = map(int, input().split())
    total = 0

    for _ in range(n):
        Lww, Lwe, Lew, Lee = map(int, input().split())
        west_version = W * Lww + E * Lew
        east_version = W * Lwe + E * Lee
        total += west_version if west_version >= east_version else east_version

    out.append(f"Data Set {ds}:")
    out.append(str(total))
    out.append("")

print("\n".join(out))
