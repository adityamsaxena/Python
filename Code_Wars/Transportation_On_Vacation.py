'''
After a hard quarter in the office you decide to get some rest on a vacation. So you will book a flight for you and your girlfriend 
and try to leave all the mess behind you.
You will need a rental car in order for you to get around in your vacation. The manager of the car rental makes you some good offers.
Every day you rent the car costs $40. If you rent the car for 7 or more days, you get $50 off your total. Alternatively, 
if you rent the car for 3 or more days, you get $20 off your total.

Write a code that gives out the total amount for different days(d).
'''

def rental_car_cost(days):
    rent_of_car = 40
    if days not in range(1,7):
        print((days * rent_of_car) - 50) 
    elif days in range(3,7) :
        print((days * rent_of_car) - 20) 
    else:
        print(rent_of_car)
rental_car_cost(23) 