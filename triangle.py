def is_valid_triangle(a, b, c) -> bool:
    # Check if all sides are positive
    if a <=0 or b<=0 or c<=0:
        return False
    # Check the triangle inequality
    if a + b <= c or a + c <= b or b + c <= a:
        return False
    else:
        return True

def classify_triangle(a,b,c) -> str:
    
    result = ""
    # Classify the triangle based on the lengths of its sides
    if not is_valid_triangle(a, b, c):
        result = "Invalid triangle"
    elif a == b == c:
        result = "Equilateral"
    elif a == b or b == c or a == c:
        result += "Isosceles"
    else:
        result += "Scalene"
    # An additional check for right triangle: Note that an equilateral triangle cannot be a right traingle.
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        result = "Right" + " " + result

    return result
