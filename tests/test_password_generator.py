import unittest
from src.password_generator import PasswordGenerator

class TestPasswordGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = PasswordGenerator()

    def test_default_password_length(self):
        password = self.generator.generate_password()
        self.assertEqual(len(password), 12)

    def test_custom_password_length(self):
        length = 16
        password = self.generator.generate_password(length=length)
        self.assertEqual(len(password), length)

    def test_minimum_length_requirement(self):
        with self.assertRaises(ValueError):
            self.generator.generate_password(length=7)

    def test_os_random_generation(self):
        password = self.generator.generate_password(use_os_random=True)
        self.assertEqual(len(password), 12)

if __name__ == '__main__':
    unittest.main()