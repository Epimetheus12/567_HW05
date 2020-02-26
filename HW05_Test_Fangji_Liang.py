'''
Test for HW05
Fangji Liang
'''
from HW05_Fangji_Liang import classify_triangle, classify_triangle_bug
import unittest
import math as m


class TestTriangles(unittest.TestCase):
    '''
    Test cases for classify_triangle
    '''

    def test_classify_triangle(self):
        self.assertEqual(classify_triangle(1, 1, 2), False)
        self.assertEqual(classify_triangle(1.1, 1.1, 2), "Isosceles")
        self.assertEqual(classify_triangle(
            m.sqrt(2), m.sqrt(2), 2), "RightIsosceles")
        self.assertEqual(classify_triangle(1, 1, 1), "Equilateral")
        self.assertEqual(classify_triangle(3, 4, 5), "RightScalene")
        self.assertEqual(classify_triangle(2, 2, 3), "Isosceles")
        self.assertEqual(classify_triangle(2, 3, 4), "Scalene")
        self.assertEqual(classify_triangle(0, 1, 2), False)
        self.assertEqual(classify_triangle(-1, -2, 1), False)

    def test_classify_triangle_bug_1(self):
        '''Test case for classify_triangle_bug 1 not euqal the right answer'''
        self.assertEqual(classify_triangle_bug(1, 1, 2), False)
        self.assertNotEqual(classify_triangle_bug(
            m.sqrt(2), m.sqrt(2), 2), "RightIsosceles")
        self.assertNotEqual(classify_triangle_bug(2, 2, 3), "Isosceles")

    def test_classify_triangle_bug_2(self):
        '''Test case for classify_triangle_bug 2 not euqal the right answer'''
        self.assertNotEqual(classify_triangle_bug(1, 1, 1), "Equilateral")


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
