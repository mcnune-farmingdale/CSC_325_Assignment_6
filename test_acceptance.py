import pytest
from triangle import is_valid_triangle, classify_triangle

def acceptance(a,b,c) -> str:
    # Ensure sides are valid
    if not is_valid_triangle(a,b,c):
        return "The triangle sides are invalid."
    # Classify the triangle
    if classify_triangle(a,b,c).__contains__("Right"):
        return "This pane is a right angled piece. This requires reinforced corners."
    else: 
        return "This pane is not a right angled piece. This does not require reinforced corners."

    

def test_acceptance_invalid_triangle():
    result = acceptance(1, 2, 5)
    assert result == "The triangle sides are invalid."  # Invalid triangle

def test_acceptance_valid_triangle_not_right():
    result = acceptance(3, 3, 5)
    assert result == "This pane is not a right angled piece. This does not require reinforced corners."

def test_acceptance_right_triangle():
    result = acceptance(3, 4, 5)
    assert result == "This pane is a right angled piece. This requires reinforced corners."