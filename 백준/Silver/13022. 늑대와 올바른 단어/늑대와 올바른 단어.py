def check(word):
    i = 0
    n = len(word)
    while i < n:
        if word[i] != 'w':
            return False
        cnt = 0
        while i < n and word[i] == 'w':
            cnt += 1
            i += 1
        for ch in 'olf':
            c = 0
            while i < n and word[i] == ch:
                c += 1
                i += 1
            if c != cnt:
                return False
    return True

s = input().strip()
print(1 if check(s) else 0)
