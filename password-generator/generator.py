import random

def generate_password():
    return ''.join(chr(random.randint(33, 126)) for _ in range(8))
