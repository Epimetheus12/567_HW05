'''
Homework for 567
'''

from itertools import combinations as comb

import math as m


def classify_triangle(side_a, side_b, side_c):
    '''
    This method is to examine the three parameters is
    what kind of triangle and whether it is a triangle.
    Six kinds of triangle: RightIsosceles, Equilateral, RightScalene, Isosceles, Scalene
    and return false if the parameters can't form a triangle
    '''
    if side_a + side_b <= side_c or side_a + side_c <= side_b or side_b + side_c <= side_a:
        return False

    if side_a == side_b == side_c:
        return "Equilateral"
    temp = ''
    sides = [side_a, side_b, side_c]
    if side_a ** 2 + side_b ** 2 + side_c ** 2 == max(sides) ** 2 * 2:
        temp += "Right"
    for item in comb(sides, 2):
        if len(set(item)) == 1:
            temp += "Isosceles"
            break
    else:
        temp += "Scalene"
    return temp


def classify_triangle_bug(side_a, side_b, side_c):
    '''
    bug method
    '''
    if side_a + side_b <= side_c or side_a + side_c <= side_b or side_b + side_c <= side_a:
        return False
    
    temp = ''
    if side_a == side_b == side_c:
        temp += "Equilateral"
    sides = [side_a, side_b, side_c]
    if side_a ** 2 + side_b ** 2 + side_c ** 2 == max(sides) ** 2 * 2:
        temp += "Right"
    for item in comb(sides, 2):
        if len(set(item)) == 1:
            temp += "Isosceles"
    else:
        temp += "Scalene"
    return temp
