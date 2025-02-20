chess = {'P': 1, 'N': 3, 'B': 3, 'R': 5, 'Q': 9, 
                'p': -1, 'n': -3, 'b': -3, 'r': -5, 'q': -9}

score = 0
for _ in range(8):
    for i in input():
        score += chess.get(i, 0)

print(score)