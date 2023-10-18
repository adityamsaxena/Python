def palindrome_string(string):
    string = string.lower()
    if(string==string[::-1]):  
        print("The letter is a palindrome")  
    else:  
        print("The letter is not a palindrome")
palindrome_string('34343')