import unittest


class TestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Hook method for setting up class fixture before running tests in the class."""

    @classmethod
    def tearDownClass(cls):
        """Hook method for deconstructing the class fixture after running all tests in the class."""