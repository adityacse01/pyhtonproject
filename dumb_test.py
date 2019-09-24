import math
from unittest import TestCase
from stats import variance

class DumbTest(TestCase):
    """Some really dumb tests, to illustrate the syntax."""

    def test_identity(self):
        ZERO = 0.0
        self.assertEquals(123.5, 123.5+ZERO)
        self.assertEquals(ZERO, 123.5*ZERO)

    def test_add(self):
        self.assertEqual(2.0, 1.0+1.0)
        self.assertEqual(4.0, 2.0+2.0)

    def test_multiply(self):
        self.assertEqual(36.0, 4.0*9.0)
        # write a failing test to see how Travis CI notifies you
        # of failing builds
        #self.assertEqual(35.0, 6.0*6.0)

    def sqrt_throws_exception(self):
        # you should only test ONE STATEMENT
        # that should throw exception per "with assertRaises" block.
        # If you have more than one, there could be 
        # undetected errors -- a statement that failed
        # to throw expected exception is hidden by
        # another statement that does throw exception.
        with self.assertRaises(ValueError):
            unreal = math.sqrt(-1)
        with self.assertRaises(TypeError):
            noway = math.sqrt("1")
