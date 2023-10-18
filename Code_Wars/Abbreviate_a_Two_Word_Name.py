import string
def abbrev_name(name):
    name = string.capwords(name)
    name = list(name)
    for i in range(0,len(name)):
        if name[i] == ' ':
            print(name[0]+'.'+name[i+1])
abbrev_name('aditya saxena')