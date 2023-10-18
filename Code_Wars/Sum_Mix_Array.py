'''
Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.
Return your answer as a number.
'''

def sum_mix(arr):
    print(sum([int(x) for x in arr]))
sum_mix([1,'2',34,'100',12,'1'])