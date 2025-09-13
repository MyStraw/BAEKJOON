import sys

input = sys.stdin.readline

T = int(input())

outline = []

for i in range(T):
    N = int(input())
    line = set(map(int,input().split()))
    M = int(input())
    textbook = list(map(int, input().split()))    
    
    for k in textbook:     
           
        if k in line:
            outline.append('1')
        else :
            outline.append('0')        
            
sys.stdout.write("\n".join(outline))

