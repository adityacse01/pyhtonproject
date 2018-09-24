from unittest import TestCase
from stats import variance

class StatsTest(TestCase):

    def test_variance_typical(self):
        self.assertEqual(0.0, variance([10.0,10.0,10.0]))
        self.assertEqual(2.0, variance([1,2,3,4,5]))

    def test_variance_borderline(self):
        self.assertEqual(0.0, variance([99.999]))

    def test_variance_throws_exception(self):
        with self.assertRaises(TypeError):
            var = variance([])

if __name__ == '__main__':
    import unittest
    unittest.main(verbosity=1)

    
