import random
import string
import string_utils
import time

def generate_lower():
    l = 'abcdefghijklmnopqrstuvwxyz'
    return(l[random.randint(0,25)]+l[random.randint(0,25)])

def generate_upper():
    l = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return(l[random.randint(0,25)]+l[random.randint(0,25)])

def generate_numbers():
    l = '0123456789'
    return(l[random.randint(0,9)]+l[random.randint(0,9)])

def generate_special():
    l = string.punctuation
    return(l[random.randint(0,31)]+l[random.randint(0,31)])

def generate_password():
    lowers = generate_lower()
    uppers = generate_upper()
    numbers = generate_numbers()
    specials = generate_special()
    password = lowers + uppers + numbers + specials
    password = string_utils.shuffle(password)
    return(password)

print('Creating password')
print(30*'-')
time.sleep(1)
print('generating')
print(30*'-')
time.sleep(1)
print(generate_password()+' is your new password.')
print(30*'-')