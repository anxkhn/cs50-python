from seasons import check_birthday

def main():
    test_check_birthday()

def test_check_birthday():
    assert check_birthday("July 28, 2004") == None
    assert check_birthday("2004-7-28") == None
    assert check_birthday("2004-07-28") == ("2004", "07", "28")

if __name__ == "__main__":
    main()