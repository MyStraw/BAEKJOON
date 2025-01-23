APPLE_WEIGHT = 500  
APPLE_PRICE = 4000  
JUICE_WEIGHT = 120
JUICE_COUNT = 50    
BOX_WEIGHT_APPLE = 1000

N = int(input())
boxes = [input().split() for _ in range(N)] 
total_weight = 0
total_apple_value = 0

for box in boxes:
    T, W, H, L = box[0], int(box[1]), int(box[2]), int(box[3])
    if T == 'A':       
        apples_per_box = (W // 12) * (H // 12) * (L // 12)
        box_weight = BOX_WEIGHT_APPLE + (apples_per_box * APPLE_WEIGHT)
        total_apple_value += apples_per_box * APPLE_PRICE
    elif T == 'B':        
        box_weight = JUICE_COUNT * JUICE_WEIGHT
    else:
        continue 
    total_weight += box_weight

print(total_weight)
print(total_apple_value) 