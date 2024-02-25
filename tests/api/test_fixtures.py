import pytest

@pytest.mark.check
def test_change_name(user):
    assert user.name == 'Arthur'

@pytest.mark.check
def test_chage_second_name(user):
    assert user.second_name == 'Dent'