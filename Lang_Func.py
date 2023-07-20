def greet(lang):
    if lang == 'es':
        print('Hola')
    elif lang == 'fr':
        print("bonjour")
    else:
        print("Hello")

lang = input('Enter lang:')
greet(lang)   # call ARGUMENT(PARAMETER)