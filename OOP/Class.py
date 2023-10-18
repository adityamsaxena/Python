class Name(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def say(self):
        print("Hi, I am",self.name, "and I am", self.age,"years old")
        
    def change_age(self,age):
        self.age = age
    
aditya = Name('Aditya',23)
aadi = Name('Aadi',24)

aditya.change_age(25)

aditya.say()
aadi.say()