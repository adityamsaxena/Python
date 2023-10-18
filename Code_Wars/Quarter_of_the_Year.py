'''
Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.

For example: month 2 (February), is part of the first quarter; month 6 (June), is part of the second quarter; and month 11 (November),
is part of the fourth quarter.

Constraint:
1 <= month <= 12
'''

def quarter_of(month):
    if month in [1,2,3]:
        print(1) 
    elif month in [4,5,6]:
        print(2) 
    elif month in [7,8,9]:
        print(3) 
    elif month in [10,11,12]:
        print(4) 
    else:
        print(False) 
    quarter_of(5)