s = input()
i = 0
res = []

while i < len(s):
    res.append(s[i])
    i += ord(s[i]) - ord('A') + 1

print("".join(res))