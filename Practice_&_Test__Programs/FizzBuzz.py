
def fizz_buzz(num):
    for n in range(num):
        if n%3 == 0 and n%5 == 0:
            print('fizz buzz')
        elif n%3 == 0:
            print('fizz')
        elif n%5 == 0:
            print('buzz')
        else: 
            print(n)

fizz_buzz(101)