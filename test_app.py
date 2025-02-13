import unittest
from app import add_numbers 

class TestSumFunction(unittest.TestCase):

    def test_negative_sum(self):
        """Test if adding negative numbers returns correct result"""
        result = add_numbers(-10, -20)
        self.assertEqual(result, -35)

if __name__ == '__main__':
    unittest.main()
