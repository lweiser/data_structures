"""Unit tests for my implmentations of linked_lists."""


import linked_lists as ll
import unittest


def push_front_all(in_list):
    """Push all values in a list into a linked list."""
    out_llist = ll.SinglyLinkedList()
    for val in in_list:
        out_llist.push_front(val)
    return out_llist


def push_back_all(in_list):
    """Push all values in a list into a linked list."""
    out_llist = ll.SinglyLinkedList()
    for val in in_list:
        out_llist.push_back(val)
    return out_llist


def pop_front_all(in_llist):
    """Convert a linked list into list by popping all values from the front."""
    out_list = []
    while True:
        val = in_llist.pop_front()
        if val is None:
            break
        out_list.append(val)
    return out_list


def pop_back_all(in_llist):
    """Convert a linked list into list by popping all values from the back."""
    out_list = []
    while True:
        val = in_llist.pop_back()
        if val is None:
            break
        out_list.append(val)
    return out_list


class TestIsEmpty(unittest.TestCase):
    """Test empty initialization and isempty function."""

    def setUp(self):
        """Initialize an empty list."""
        self.llist = ll.SinglyLinkedList()

    def test_empty_init(self):
        """Test initalized to empty."""
        self.assertIsNone(self.llist._head)
        self.assertIsNone(self.llist._tail)

    def test_isempty(self):
        """Test that isempty() returns empty on list."""
        self.assertTrue(self.llist.is_empty())


class TestPush(unittest.TestCase):
    """Test push_front and push_back functions."""

    def setUp(self):
        """Start from an empty list."""
        self.llist = ll.SinglyLinkedList()

    def test_empty_push_front(self):
        """Test push_front on empty list."""
        self.llist.push_front('A')
        self.assertEqual(self.llist._head.value, 'A')
        self.assertEqual(self.llist._tail.value, 'A')
        self.assertIsNone(self.llist._tail.next)

    def test_empty_push_back(self):
        """Test that push_back adds correctly to an empty list."""
        self.llist.push_back('A')
        self.assertEqual(self.llist._head.value, 'A')
        self.assertEqual(self.llist._tail.value, 'A')
        self.assertIsNone(self.llist._tail.next)

    def test_push_front_one_element(self):
        """Test that push_front adds correctly to a one element list."""
        self.llist.push_front('A')
        self.llist.push_front('B')
        self.assertEqual(self.llist._head.value, 'B')
        self.assertEqual(self.llist._tail.value, 'A')
        self.assertEqual(self.llist._head.next.value, 'A')

    def test_push_back_one_element(self):
        """Test that push_front adds correctly to a one element list."""
        self.llist.push_front('A')
        self.llist.push_back('C')
        self.assertEqual(self.llist._head.value, 'A')
        self.assertEqual(self.llist._tail.value, 'C')
        self.assertEqual(self.llist._head.next.value, 'C')
        self.assertIsNone(self.llist._tail.next)

    def test_push_back_three_elements(self):
        """Test that push_back adds correctly when called multiple times."""
        self.llist.push_back('A')
        self.llist.push_back('B')
        self.llist.push_back('C')
        self.llist.push_back('D')
        self.assertEqual(self.llist._head.value, 'A')
        self.assertEqual(self.llist._tail.value, 'D')
        self.assertEqual(self.llist._head.next.value, 'B')
        self.assertIsNone(self.llist._tail.next)

    def test_push_front_three_elements(self):
        """Test that push_front adds correctly when called multiple times."""
        self.llist.push_front('A')
        self.llist.push_front('B')
        self.llist.push_front('C')
        self.llist.push_front('D')
        self.assertEqual(self.llist._head.value, 'D')
        self.assertEqual(self.llist._tail.value, 'A')
        self.assertEqual(self.llist._head.next.value, 'C')
        self.assertIsNone(self.llist._tail.next)


class Test_List_Modification(unittest.TestCase):
    """Test push_front and push_back functions."""

    elements = ['A', 'B', 'C', 'D', 'E']

    def setUp(self):
        """Start from an empty list."""
        self.llist = push_back_all(self.elements)

    def test_top_front(self):
        """Test top_back behaves appropriately."""
        self.assertEqual(self.llist.top_front(), 'A')
        self.assertEqual(self.llist._head.value, 'A')
        self.assertEqual(pop_front_all(self.llist), self.elements)

    def test_top_back(self):
        """Test top_back behaves appropriately."""
        self.assertEqual(self.llist.top_back(), 'E')
        self.assertIsNone(self.llist._tail.next)
        self.assertEqual(pop_front_all(self.llist), self.elements)

    def test_pop_front(self):
        """Test pop_front returns correct value and modifies list."""
        self.assertEqual(self.llist.pop_front(), 'A')
        self.assertEqual(self.llist._head.value, 'B')
        self.assertEqual(pop_front_all(self.llist), ['B', 'C', 'D', 'E'])

    def test_pop_back(self):
        """Test pop_back returns correct value and modifies list."""
        self.assertEqual(self.llist.pop_back(), 'E')
        self.assertEqual(self.llist._tail.value, 'D')
        self.assertIsNone(self.llist._tail.next)
        self.assertEqual(pop_front_all(self.llist), ['A', 'B', 'C', 'D'])

    def test_erase_front(self):
        """Test an erase at the front of the list."""
        self.llist.erase('A')
        self.assertEqual(pop_front_all(self.llist), ['B', 'C', 'D', 'E'])

    def test_erase_back(self):
        """Test an erase at the back."""
        self.llist.erase('E')
        self.assertEqual(pop_front_all(self.llist), ['A', 'B', 'C', 'D'])

    def test_erase_middle(self):
        """Test an erase in the middle."""
        self.llist.erase('C')
        self.assertEqual(pop_front_all(self.llist), ['A', 'B', 'D', 'E'])

    def test_erase_absent(self):
        """Test an erase called for a value not in the list."""
        self.llist.erase('X')
        self.assertEqual(pop_front_all(self.llist), self.elements)

    def test_add_before_front(self):
        """Test add before when the target value is the first value."""
        self.llist.add_before('A', 'X')
        self.assertEqual(pop_front_all(self.llist),
                         ['X', 'A', 'B', 'C', 'D', 'E'])

    def test_add_before_end(self):
        """Test add before when the target value is the last value."""
        self.llist.add_before('E', 'X')
        self.assertEqual(pop_front_all(self.llist),
                         ['A', 'B', 'C', 'D', 'X', 'E'])

    def test_add_before_middle(self):
        """Test add before when the target value is the middle value."""
        self.llist.add_before('C', 'X')
        self.assertEqual(pop_front_all(self.llist),
                         ['A', 'B', 'X', 'C', 'D', 'E'])

    def test_add_before_absent(self):
        """Test add before when the target value is the middle value."""
        self.llist.add_before('Y', 'X')
        self.assertEqual(pop_front_all(self.llist), self.elements)

    def test_add_after_front(self):
        """Test add before when the target value is the first value."""
        self.llist.add_after('A', 'X')
        self.assertEqual(pop_front_all(self.llist),
                         ['A', 'X', 'B', 'C', 'D', 'E'])

    def test_add_after_end(self):
        """Test add before when the target value is the last value."""
        self.llist.add_after('E', 'X')
        self.assertEqual(pop_front_all(self.llist),
                         ['A', 'B', 'C', 'D', 'E', 'X'])

    def test_add_after_middle(self):
        """Test add before when the target value is the middle value."""
        self.llist.add_after('C', 'X')
        self.assertEqual(pop_front_all(self.llist),
                         ['A', 'B', 'C', 'X', 'D', 'E'])

    def test_add_after_absent(self):
        """Test add before when the target value is the middle value."""
        self.llist.add_after('Y', 'X')
        self.assertEqual(pop_front_all(self.llist), self.elements)

    def test_reverse_reverses(self):
        """Test reverse in place."""
        self.llist.reverse_in_place()
        self.assertIsNone(self.llist._tail.next)
        self.assertEqual(self.llist._head.value, 'E')
        self.assertEqual(self.llist._tail.value, 'A')
        self.assertEqual(pop_front_all(self.llist),
                         [e for e in reversed(self.elements)])

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
