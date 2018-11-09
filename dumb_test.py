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
        self.assertEqual(35.0, 6.0*6.0)
