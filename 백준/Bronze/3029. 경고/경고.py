now = input()
target = input()

h1, m1, s1 = map(int, now.split(':'))
h2, m2, s2 = map(int, target.split(':'))

t1 = h1 * 3600 + m1 * 60 +s1
t2 = h2 * 3600 + m2 * 60 +s2

diff = t2 - t1
if diff <= 0:
    diff +=24*3600

h = diff // 3600
diff %= 3600
m = diff // 60
s = diff % 60

print(f"{h:02d}:{m:02d}:{s:02d}")