from generator import generate_password

def test_generate_password():
    pwd = generate_password()
    assert len(pwd)==8
    assert all(33 <= ord(c) <= 126 for c in pwd)
    assert pwd != generate_password()