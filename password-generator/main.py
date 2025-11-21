import generator
import validator

password = next(temp for temp in iter(generator.generate_password, None) if validator.password_validator(temp))

print(f'votre nouveau mot de passe est :  {password}')