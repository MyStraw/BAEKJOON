N_K = input()
N, K = map(int, N_K.split())
X_input = input()
X= X_input.split()
X= list(map(int, X))

i= 0
count = 0

while (i<N):
    count = count+1
    end = X[i] + K
    while(i<N and X[i]<=end):
        i = i+1
    
print(count)