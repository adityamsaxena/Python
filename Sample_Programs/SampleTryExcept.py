str = input('Enter a number: ')
try:
    ivalue = int(str)
except:
    ivalue = -1

    if ivalue > 0 :
        print('Nice Work')
    else:
        print('Not a Number')
