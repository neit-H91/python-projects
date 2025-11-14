import generator
import validator

password = ''

while True:
    temp = generator.generate_password()
    if validator.password_validator(temp):
        password = temp
        break

print(f'votre nouveau mot de passe {password}')