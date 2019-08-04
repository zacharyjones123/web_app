import unittest
from karalibraryapp.isbn_processor import *

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

    def test_clean_isbn(self):
        new_input = ["9780764526411", "9780764526412", "9780764526412",
                     "9780764526412", "9780764526412", "9780764526412",
                     "9780764526412", "9780764526412", "9780764526412",
                     "9781861978761", "9781861978762", "9781861978763",
                     "9781861978764", "9781861978765", "9781861978766",
                     "9781861978767", "9781861978768", "9781861978769"]
        output = ["9780764526411",           "",              "",
                  "",           "",              "",
                  "",           "",              "",
                  "",           "",              "",
                  "",           "",              "",
                  "",           "", "9781861978769"]
        for inn, out in zip(new_input, output):
            self.assertEqual(clean_isbn(inn), out)

    @unittest.skip("WIP")
    def test_get_data_1(self):
        self.assertEqual(True, True)

    @unittest.skip("WIP")
    def test_write_book_to_file(self):
        self.assertEqual(True, True)

    @unittest.skip("WIP")
    def test_process_isbns(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
