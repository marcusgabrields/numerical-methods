"""Tests for the bisection algorithm for Numerical Methods course"""

from math import cos, sin, exp, tan
from unittest import TestCase

from bisection import bisection


class BisectionTest(TestCase):

    def test_sin_bisection(self):
        result = bisection(sin, [-2, 3], 1e-03)
        self.assertEqual(-0.00018310546875, result)
    
    def test_cos_bisection(self):
        result = bisection(cos, [-2, 1], 1e-03)
        self.assertEqual(-1.5704345703125, result)
    
    def test_exp_plus_tan(self):
        f = lambda x: exp(x) + tan(x)
        
        result = bisection(f, [-1, 0], 1e-03)
        self.assertEqual(-0.53173828125, result)
