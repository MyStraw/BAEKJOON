total_loss = 0
bet = int(input())

while bet != -1:
    total_loss += bet
    bet = int(input())

print(total_loss)