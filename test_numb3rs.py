from numb3rs import validate

def test_shorten():
    assert validate("192.168.43.1") == True
    assert validate("0.0.0.0") == True
    assert validate("17.15.21.10") == True
    assert validate("256.0.0.1") == False
