import sys
input = sys.stdin.readline
outline = []
N = int(input())
line = set(map(int,input().split()))
M = int(input())
contain = list(map(int,input().split()))
for c in contain:               
    outline.append('1' if c in line else '0')        
sys.stdout.write("\n".join(outline))


    
