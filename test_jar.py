from jar import Jar

def main():
    test_init()
    test_str()
    test_deposit()

def test_init():
    jar_one = Jar()
    assert jar_one.capacity == 12
    jar_two = Jar(5)
    assert jar_two.capacity == 5

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(10)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5

def test_withdraw():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(4)
    assert jar.size == 1