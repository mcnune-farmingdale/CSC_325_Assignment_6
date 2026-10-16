import pytest
import math
from triangle import is_valid_triangle, classify_triangle

def test_is_valid_triangle():
    # Test valid triangles
    assert is_valid_triangle(3, 4, 5) == True
    assert is_valid_triangle(5, 5, 5) == True
    assert is_valid_triangle(2, 2, 3) == True

def test_is_invalid_triangle(): 
    # Test invalid triangles
    assert is_valid_triangle(1, 2, 3) == False
    assert is_valid_triangle(0, 4, 5) == False
    assert is_valid_triangle(-1, 4, 5) == False

def test_classify_right_scalene_triangle():
    # Test valid triangles
    assert classify_triangle(3, 4, 5) == "Right Scalene"
   
def test_classify_scalene_triangle():
    #Test scalene triangle
    assert classify_triangle(3, 4, 6) == "Scalene"
    assert classify_triangle(5, 6, 7) == "Scalene"

def test_classify_isosceles_triangle():
    #Test isosceles triangle
    assert classify_triangle(2, 2, 3) == "Isosceles"
    assert classify_triangle(5, 5, 8) == "Isosceles"

def test_classify_equilateral_triangle():
    #Test equilateral triangle
    assert classify_triangle(5, 5, 5) == "Equilateral"
    assert classify_triangle(10, 10, 10) == "Equilateral"