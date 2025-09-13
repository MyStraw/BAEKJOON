import sys
input = sys.stdin.readline
outline = []
N = int(input())
line = set(map(int,input().split()))
M = int(input())
contain = list(map(int,input().split()))
for c in contain:               
    if c in line:
        outline.append('1')
    else:
        outline.append('0')  
sys.stdout.write("\n".join(outline))


    
