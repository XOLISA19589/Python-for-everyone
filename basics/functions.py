#function acts like a variables, it stores codes

def my_function():
    print('Hello from a function')
my_function()

def get_greeting():
    return 'Hello from a function'
message = get_greeting()
print(message)


def get_greeting():
    return 'Hello from a function'
print(get_greeting())


def greet(lang):
    if lang == 'es':
        print('Hola')
    elif lang == 'fr':
        print('Bojo')
    else:
        print('hello')
    
greet('es')
greet('fr')
greet('en')

def my_function(fname):
    print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")