import unittest
import four

class Test_greeter_function(unittest.TestCase):

    def test_if_empty_name(self):
        self.assertEqual(four.greeter(''), 'Hello, Mr Nobody!')

    def test_with_name(self):
        self.assertEqual(four.greeter('Anna Török'), 'Hello, Anna Török!')


if __name__ == '__main__':
    unittest.main()
