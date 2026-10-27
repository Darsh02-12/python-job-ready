
from linked_list import LinkedList


def test_append():
    linked_list = LinkedList()
    linked_list.append(10)
    linked_list.append(20)

    assert linked_list.to_list() == [10, 20]


def test_prepend():
    linked_list = LinkedList()
    linked_list.append(10)
    linked_list.prepend(5)

    assert linked_list.to_list() == [5, 10]


def test_reverse():
    linked_list = LinkedList()
    linked_list.append(10)
    # linked_list.append(20)
    # linked_list.append(30)
    linked_list.reverse()
    
    assert linked_list.to_list() == [10]

def test_reverse_two():
    linked_list = LinkedList()
    linked_list.append(10)
    linked_list.append(20)
    # linked_list.append(30)
    # linked_list.reverse()
    linked_list.reverse()
    assert linked_list.to_list() == [20,10]

def test_empty_list():
    linked_list = LinkedList()

    assert linked_list.to_list() == []