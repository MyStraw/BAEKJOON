R, C = map(int, input().split())

farm = []

garo_cnt = 0
sero_cnt = 0
garo_hole_cnt = 0
sero_hole_cnt = 0
garo_dung_cnt = 0
sero_dung_cnt = 0

for k in range(R):
    farm.append(input())
    garo_flag = False    
    dung = False
        
    for _ in farm[k]:
        for i in _:
            if i =='#' and garo_flag == True and dung == True:              
                garo_dung_cnt +=1
            if i =='#' and garo_flag == True and dung == False:                        
                garo_cnt +=1                                            
                dung = True    
           
            if i == '#':
                garo_hole_cnt +=1
                garo_flag = True                    
            elif i == '.':
                garo_flag = False
                dung = False
                
dung = False   
for c in range(C):
    sero_flag = False     
    for r in range(R):
        if farm[r][c] == '#' and sero_flag == True and dung == True:  
            sero_dung_cnt +=1
        if farm[r][c] == '#' and sero_flag == True and dung == False:                   
            sero_cnt +=1            
            dung = True
        
        if farm[r][c] == '#':
            sero_hole_cnt +=1
            sero_flag = True  
        
        elif farm[r][c] == '.':
            sero_flag = False
            dung = False


print(garo_hole_cnt -(garo_cnt + sero_cnt) - (garo_dung_cnt+sero_dung_cnt))

     
