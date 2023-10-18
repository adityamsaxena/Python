def pig_latin(string):
    string = string.lower()
    vowel = 'aeiou'
    if string[0] in vowel:
        print(string+'way')
    else:
        print(string[1:]+string[0] +'ay')
pig_latin('hanu')