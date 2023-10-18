numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

two_more_num = [x for x in numbers if x not in range(x,10)]

print(two_more_num)