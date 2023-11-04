import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    """Tests for function (name_function)"""

    def test_first_last_name(self):
        """names like: Janis and Joplin -> working right?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, "Janis Joplin")

if __name__ == '__main__':
    unittest.main()
