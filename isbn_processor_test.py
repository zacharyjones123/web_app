import unittest
from isbn_processor import *

"""
Each test case should follow:
Arrange - Set up the object to be tested & collaborators
Act - Exercise functionality on the object
Assert - Make claims about the object & its collaborators
Cleanup - Release resources, restore to original state (tearDown)

setUp and tearDown are called "test fixtures"

Each test should only test one behavior
or one reason to fail


"""


class MyTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_suite_test(self):
        self.assertEqual(True, True)

    def test_clean_isbn(self):
        new_input = ["978-0-7645-2641-1", "0764526413"]
        output = ["9780764526411", "9780764526411"]
        for inn, out in zip(new_input, output):
            self.assertEqual(clean_isbn(inn), out)

    def test_clean_isbn_1(self):
        self.assertEqual(clean_isbn("978-0-7645-2641-1"), "9780764526411")

    def test_clean_isbn_2(self):
        self.assertEqual(clean_isbn("978-0764526411"), "9780764526411")

    def test_clean_isbn_3(self):
        self.assertEqual(clean_isbn("9780764526411"), "9780764526411")

    def test_clean_isbn_4(self):
        self.assertEqual(clean_isbn("0764526413"), "9780764526411")

    def test_get_data_1(self):
        self.assertEqual(True, True)

    def test_write_book_to_file(self):
        self.assertEqual(True, True)

    def test_process_isbns(self):
        self.assertEqual(True, True)

    @unittest.skip("WIP")
    def test_clean_isbn_5(self):
        pass

if __name__ == '__main__':
    unittest.main()
