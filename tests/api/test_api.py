class User:

    def __init__(self) -> None:
        self.name = "Anastasiia"
        self.second_name = "Kovalenko"

user = User()

def test_remove_name():
    user.name = ''
    assert user.name == ''

def test_name():
    assert user.name == "Anastasiia"

def test_name():
    assert user.second_name == "Kovalenko"