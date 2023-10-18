count =0
sum = 0
print('Before Count', count)

for num in [9,41,3,13,14,120,1000]:
    
    sum = num + sum
    count = count + 1
    print(count, sum)
    
print('Total Sum is =',sum)
#print('Average =', sum/count)