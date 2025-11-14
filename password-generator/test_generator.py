from generator import generate_password
from unittest import mock


def test_generate_password_length_and_characters():
    pwd = generate_password()
    assert len(pwd) == 8
    assert all(33 <= ord(c) <= 126 for c in pwd)

def test_generate_password_deterministic():
    with mock.patch('random.randint', side_effect=[65]*8):
        pwd = generate_password()
        assert pwd == 'AAAAAAAA'
