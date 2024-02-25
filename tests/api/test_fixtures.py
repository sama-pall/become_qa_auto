import pytest


class User:
    def __init__(self):
        self.name = None
        self.second_name = None

    def create(self):
        self.name = 'Arthur'
        self.second_name = 'Dent'

    def remove(self):
        self.name = ''
        self.second_name = ''


@pytest.fixture
def user():
    user = User()

    user.create()
    yield user
    user.remove()
def test_change_name(user):
    assert user.name == 'Arthur'

def test_chage_second_name(user):
    assert user.second_name == 'Dent'