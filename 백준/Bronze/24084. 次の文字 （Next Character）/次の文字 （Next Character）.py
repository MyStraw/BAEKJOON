N = int(input())
S = input()

for i in range(1, N):
    if S[i] == 'J':
        print(S[i-1])
