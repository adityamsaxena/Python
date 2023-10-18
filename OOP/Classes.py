x = 'string'
y = 23
bool = True

class number():
    
    def__init__(self, num):
        self.var = num
        
    def display(self, x):
        print(x)
        
num = number(23)
print(num) #this statement gives o/p of object address

num.display(num.var) #method for calling class