import unittest

from problem_6.exceptions import BadCollectionType, BadArgumentException
from problem_6.list_adder import ListAdder


class TestListAdder(unittest.TestCase):

    def test_add(self):
        list_add = ListAdder([])
        result = list_add.add([1, 2, "Three"], [4, 5, "Four"])
        self.assertEqual([1, 2, "Three", 4, 5, "Four"], result)

    def test_bad_collection_type(self):
        try:
            list_add = ListAdder()
        except BadCollectionType as e:
            self.assertEqual(type(e), BadCollectionType)
        else:
            self.fail("'BadCollectionType' not raised.")

    def test_empty_argument(self):
        try:
            list_add = ListAdder([])
            a = list_add.add([1, 2, "Three"], None)
        except BadArgumentException as e:
            self.assertEqual(type(e), BadArgumentException)
            self.assertEqual(e.message, "Provided argument is empty.")
        else:
            self.fail("'BadArgumentException' not raised.")


if __name__ == '__main__':
    unittest.main()
