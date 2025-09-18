import sys
input = sys.stdin.readline
N = int(input())

cards = {}

for i in range(N):    
    val = int(input())
    cards.setdefault(val, 0)    
    cards[val] += 1
        
maxK = 0
maxV = 0

for key in sorted(cards):
    value = cards[key]
    if maxV < value:        
        maxV = value
        maxK = key
    
print(maxK)
