import re

def number_validator(str):
    pattern = r'^(?:\D*\d){2}\D*$'
    return(re.fullmatch(pattern,str) is not None)

def lower_validator(str):
    pattern = r'^(?:[^a-z]*[a-z]){2}[^a-z]*$'
    return(re.fullmatch(pattern,str) is not None)

def upper_validator(str):
    pattern = r'^(?:[^A-Z]*[A-Z]){2}[^A-Z]*$'
    return(re.fullmatch(pattern,str) is not None)

def punctuation_validator(str):
    pattern = r'^(?:[^!-/:-@[-`{-~]*[!-/:-@[-`{-~]){2}[^!-/:-@[-`{-~]*$'
    return(re.fullmatch(pattern,str) is not None)

def password_validator(str):
    return(punctuation_validator(str) and upper_validator(str) and lower_validator(str) and number_validator(str))