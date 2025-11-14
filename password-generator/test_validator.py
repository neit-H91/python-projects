from validator import number_validator,lower_validator,upper_validator,punctuation_validator, password_validator

def test_number_validator():
    assert number_validator('12')
    assert not number_validator('123')
    assert not number_validator('1')
    assert not number_validator('ab')
    assert number_validator('') == False

def test_lower_validator():
    assert lower_validator('abC')
    assert not lower_validator('abc')
    assert not lower_validator('AB')
    assert not lower_validator('aB')
    assert lower_validator('') == False

def test_upper_validator():
    assert upper_validator('ABc')
    assert not upper_validator('Abc')
    assert not upper_validator('ABC')
    assert not upper_validator('abc')
    assert upper_validator("") == False

def test_punctuation_validator():
    assert punctuation_validator('!?')
    assert not punctuation_validator('!?.')
    assert not punctuation_validator('.')
    assert punctuation_validator('') == False

def test_password_validator():
    assert password_validator('"7kzX4\'X')
    assert not password_validator('"7kzX4X')
    assert not password_validator('"7kzX4\'')
    assert not password_validator('"7kzX\'X')
    assert not password_validator('"7kX4\'X')
    assert password_validator('') == False