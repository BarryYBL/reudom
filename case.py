import unittest
import time


class TestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Hook method for setting up class fixture before running tests in the class."""

    @classmethod
    def tearDownClass(cls):
        """Hook method for deconstructing the class fixture after running all tests in the class."""

def millisecond():
    """Get millisecond timestamp"""
    times = time.time()
    milliSecond = int(times * 1000)
    return milliSecond

def seconds():
    """Get second time stamp"""
    times = time.time()
    Seconds = int(times * 10000)
    return Seconds
