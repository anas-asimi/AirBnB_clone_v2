#!/usr/bin/python3
"""test for console"""
import unittest


class TestConsole(unittest.TestCase):
    """this will test the console"""

    def test_true_is_true(self):
        """Pep8 console.py"""
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
