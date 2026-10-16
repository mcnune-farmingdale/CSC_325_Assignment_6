from triangle import is_valid_triangle, classify_triangle

def test_is_valid_triangle():
    # Test valid triangles
    assert is_valid_triangle(3, 4, 5) == True
    assert is_valid_triangle(5, 5, 5) == True
    assert is_valid_triangle(2, 2, 3) == True

    # Test invalid triangles
    assert is_valid_triangle(1, 2, 3) == False
    assert is_valid_triangle(0, 4, 5) == False

def test_classify_triangle():
    # Test valid triangles
    assert classify_triangle(3, 4, 5) == "Right Scalene"
    assert classify_triangle(5, 5, 5) == "Equilateral"
    assert classify_triangle(2, 2, 3) == "Isosceles"
    assert classify_triangle(3, 4, 6) == "Scalene"
    assert classify_triangle(5, 5, 5 * math.sqrt(2)) == "Right Isosceles"

    # Test invalid triangles
    assert classify_triangle(1, 2, 3) == "Invalid triangle"
    assert classify_triangle(0, 4, 5) == "Invalid triangle"
    assert classify_triangle(-1, 4, 5) == "Invalid triangle"