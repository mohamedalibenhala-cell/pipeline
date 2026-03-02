import pytest
from app.usermanager import UserManager

def test_add_user():
    manager = UserManager()
    manager.add_users("adam")
    assert manager.count_users() == 1

def test_add_existing_user():
    manager = UserManager()
    manager.add_users("adam")
    with pytest.raises(ValueError):
        manager.add_users("adam")

def test_remove_user():
    manager = UserManager()
    manager.add_users("youssef")
    manager.remove_user("youssef")
    assert manager.count_users() == 0

def test_remove_unkown_user():
    manager = UserManager()
    with pytest.raises(ValueError):
        manager.remove_user("saad")