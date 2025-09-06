import sys

input = sys.stdin.readline

N = int(input().strip())
cards = list(map(int, input().split()))
cards.sort()

M = int(input().strip())
queries = list(map(int, input().split()))

def count_occurrences(a, x):
    l, r = 0, len(a)
    while l < r:
        m = (l + r) // 2
        if a[m] < x:
            l = m + 1
        else:
            r = m
    left = l
    l, r = 0, len(a)
    while l < r:
        m = (l + r) // 2
        if a[m] <= x:
            l = m + 1
        else:
            r = m
    right = l
    return right - left

print(' '.join(str(count_occurrences(cards, q)) for q in queries))