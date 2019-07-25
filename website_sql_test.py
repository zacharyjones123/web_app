import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_insert_into_database(self):
        self.assertEqual(True, True)

    def test_select_from_database(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
