import re
from generator import generate_lower,generate_upper,generate_numbers,generate_special
import string

def test_generate_lower():
    sample = generate_lower()

    lowers = re.findall(r'[a-z]', sample)

    assert len(lowers) == 2

def test_generate_upper():
    sample = generate_upper()

    uppers = re.findall(r'[A-Z]',sample)

    assert len(uppers)==2

def test_generate_numbers():
    sample = generate_numbers()

    numbers = re.findall(r'[0-9]',sample)

    assert len(numbers)==2

def test_generate_special():
    sample = generate_special()

    specials = re.findall(f"[{re.escape(string.punctuation)}]", sample)

    assert len(specials) == 2