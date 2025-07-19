N = int(input())

submit = []
answer = []

correct = 0
for _ in range(N):
    submit.append(input())

for a in range(N):
    if submit.pop(0) == input():
        correct += 1
        
print(correct)
    
