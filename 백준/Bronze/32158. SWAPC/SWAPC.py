n = int(input())
s = list(input())

p_idx = []
c_idx = []

for i in range(n):
    if s[i] == 'P':
        p_idx.append(i)
    elif s[i] == 'C':
        c_idx.append(i)

k = min(len(p_idx), len(c_idx))

for i in range(k):
    s[p_idx[i]], s[c_idx[i]] = s[c_idx[i]], s[p_idx[i]]

print(''.join(s))