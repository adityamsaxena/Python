smallest_num = None

for the_num in [3,9,23,50,1,20,45,-30]:
    if smallest_num is None:
        smallest_num = the_num
    elif the_num < smallest_num:
        smallest_num = the_num
    print(smallest_num,the_num)

print('Smallest number is: ',smallest_num)