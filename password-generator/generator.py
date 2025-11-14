import random

def generate_password():
    password = ''
    for i in range(8):
        password+=chr(random.randint(33,126))
    return(password)