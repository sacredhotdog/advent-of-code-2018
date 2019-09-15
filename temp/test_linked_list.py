import unittest

from temp.linked_list import LinkedList
from temp.list_item import ListItem


class TestLinkedList(unittest.TestCase):

    def test_new_list_is_empty(self):
        linked_list = LinkedList()

        self.assertEqual(len(linked_list), 0)

    def test_first_list_item_is_added_correctly(self):
        list_item = ListItem("test")
        linked_list = LinkedList()
        linked_list.append(list_item)

        self.assertEqual(linked_list[0], list_item)

