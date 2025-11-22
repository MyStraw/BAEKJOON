N = int(input())

diff = N - 2013

heaven = (9 + diff) % 10
earth = (5 + diff) % 12

print(chr(ord('A') + earth) + str(heaven))
