def ip_add_validation(n):
    num = n.split(".")
    
    if len(num)!=4:
        
        print('False')
    else:
        print('True')
    
    for number in num:
        if not isinstance(int(number), int):
            print('false')
        if int(number) < 0 or int(number) > 255:
            print('falsee')
    print('true')
ip_add_validation('a20.120.120.255')

'''
def ip_add_validation(n):
    ip_list = n.split(".")
    
    if len(ip_list)!=4:
        return False
    
    for element in ip_list:
        try:
            if not isinstance(int(element), int):
                return False
            if int(element) < 0 or int(element) > 255:
                return False
        except:
            print('Invalid IP Address')
ip_add_validation('120.120.120.255')
'''