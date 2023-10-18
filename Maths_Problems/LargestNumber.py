largest_num = -1
print('Before', largest_num)

for the_num in [4,74,41,50,15,120]:
    if the_num > largest_num:
        largest_num = the_num 
        
    print(largest_num,the_num)
        
print('After',largest_num)

