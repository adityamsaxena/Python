if __name__ == '__main__':
    s = input()
    alnum = alpha = digit = lower = upper = False
    
    for i in s:
        if(i.isalpha()):
            alpha = i.isalpha()
        if(i.isalnum()):
            alnum = i.isalnum()
        if(i.isdigit()):
            digit = i.isdigit()
        if(i.isupper()):
            upper = i.isupper()
        if(i.islower()):
            lower = i.islower()
    print(alnum)
    print(alpha)
    print(digit)
    print(lower)
    print(upper)