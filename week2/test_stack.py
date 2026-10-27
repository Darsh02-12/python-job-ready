import pytest
from stack import Stack, StackEmptyError


def test_pop_empty_stack_raises_error():
    stack = Stack()

    with pytest.raises(StackEmptyError):
        stack.pop()
