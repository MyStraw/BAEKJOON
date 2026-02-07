N = input()
length = len(N)

left_total = 0
right_total = 0
for i in range(length):
    if i <= (length/2)-1:
        left_total += int(N[i])
    else:
        right_total +=int(N[i])
        
if left_total == right_total:
    print("LUCKY")
else:
    print("READY")
