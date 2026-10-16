from triangle import is_valid_triangle, classify_triangle

def test_acceptance(a,b,c):
    # Ask for user for triangle sides
    valid = False
    # Ensure sides are valid
    if is_valid_triangle(a,b,c):
        valid = True
    else:
        print("The triangle sides are invalid.")
        return valid
    
    # Classify the triangle
    if classify_triangle(a,b,c).__contains__("Right"):
        print("This pane is a right angled piece. This requires reinforced corners.")
    else: 
        print("This pane is not a right angled piece. This does not require reinforced corners.")

def test_acceptance_invalid_triangle():
    test_acceptance(1, 2, 5) 
    captured = capsys.readouterr() #Read the output
    assert captured.out == "The triangle sides are invalid.\n"  # Invalid triangle

def test_acceptance_valid_triangle_not_right():
    test_acceptance(3, 4, 5) 
    captured = capsys.readouterr() #Read the output
    assert captured.out == "This pane is not a right angled piece. This does not require reinforced corners.\n"

def test_acceptance_right_triangle():
    test_acceptance(3, 4, 5) 
    captured = capsys.readouterr() #Read the output
    assert captured.out == "This pane is a right angled piece. This requires reinforced corners.\n"