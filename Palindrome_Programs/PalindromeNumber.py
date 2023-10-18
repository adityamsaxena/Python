def palindrome_num(num):
    temp = num  
    rev = 0  
    while(num > 0):  
        dig = num % 10  
        rev = rev * 10 + dig  
        num = num // 10  
    if(temp == rev):  
        print("This value is a palindrome number!")  
    else:  
        print("This value is not a palindrome number!") 
palindrome_num(4544)