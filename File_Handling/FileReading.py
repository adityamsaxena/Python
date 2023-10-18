file = open('ReadFile.txt.txt','r')
f = file.readlines()
#print(f)

#for removing backslash(/n) from o/p, we use 'for loop':
# -1 indicates the last element in a list/string
# 'line' is a reserved word

newList = []

'''for line in f:
    if line[-1] == '\n':
        newList.append(line[:-1])
    else:
        newList.append(line)'''

# easy method:

for line in f:
    newList.append(line.strip())
print(newList)

file.close()
        
