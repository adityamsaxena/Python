def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    elif lang == 'hin':
        return 'Namaste'
    else:
        return 'Hello'
    
print(greet('hin'), 'Aditya')