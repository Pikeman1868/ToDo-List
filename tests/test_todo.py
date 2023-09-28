import pytest

import todolist
from uuid import UUID

def test_test():
    assert True


class TestUserStories():
    def test_create_a_list(self):
        resp = todolist.create_list("List Name")
        assert isinstance(resp, UUID)
    
    def test_create_multiple_lists(self):
        pytest.fail("Not Implemented")

    def test_switch_lists(self):
        pytest.fail("Not Implemented")