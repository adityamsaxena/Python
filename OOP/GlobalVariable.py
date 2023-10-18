var = 9
loop = True

def Func(x):
    global loop
    
    loop =7
    
    if x==5:
        return newVar
    
def otherFunc():
    newVar = 5
    
loop = False

print(loop)