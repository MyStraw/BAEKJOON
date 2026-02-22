result = []

for i in range(1, 6):
    name = input().strip()
    if "FBI" in name:
        result.append(str(i))

if result:
    print(" ".join(result))
else:
    print("HE GOT AWAY!")