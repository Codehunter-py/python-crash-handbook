import unittest
from name_function import get_formatted_name
class NamesTestCase(unittest.TestCase):

    def test_first_last_name(self):
        """Are all names string?"""
        formatted_name = get_formatted_name('ibrahim', 'musayev')
        self.assertAlmostEqual(formatted_name, 'Ibrahim Musayev')

if __name__ == 'main':
    unittest.main()
