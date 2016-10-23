import string
import random



def generate_random_int():
    return random.randint(1, 10)
    
def generate_random_string_lower():
    return random.choice('abcdefghijklmnopqrstvxyz')


def generate_random_string_upper():
    return random.choice('ABCDEFGHIJKLMNOPQRSTVXYZ')

def generate_random_symbol():
    return random.choice('!@#$%^&*')

def generate_strong_password(passwordLen):
    return generate_password(passwordLen, True)

def get_symbols(includeSymbolsAndUpper):
    tempSymbolSaver = ""
    tempSymbolSaver = tempSymbolSaver + str(generate_random_int())
    tempSymbolSaver = tempSymbolSaver + str(generate_random_string_lower())
    if includeSymbolsAndUpper:
        tempSymbolSaver = tempSymbolSaver + str(generate_random_string_upper())
        tempSymbolSaver = tempSymbolSaver + str(generate_random_symbol())
    return tempSymbolSaver

def generate_password(passwordLen, includeSymbolsAndUpper):
    password = get_symbols(includeSymbolsAndUpper)
    i = 4
    while i <= passwordLen:
        tempSymbolSaver = get_symbols(includeSymbolsAndUpper)
        password = password + random.choice(tempSymbolSaver)
        i = i + 1
    return random.sample(password, len(password))

def generate_weak_password(passwordLen):
    return generate_password(passwordLen, False)

def main():
    while True:
        userInput = raw_input('Enter S to generate new strong password. \nEnter W to generate new weak password. \nEnter C to exit:')
        if (userInput == 'S' or userInput == 's'):
            print(''.join(generate_strong_password(8)))
        elif(userInput == 'W' or userInput == 'w'):
            print(''.join(generate_weak_password(8)))
        elif(userInput == 'C' or userInput == 'c'):
            break
        else:
            print('Invalid data. Please try again')
        

if __name__ == '__main__':
    main()
