# Running the tests

Through Codespaces:
1. Click on the green "Code" button in the top right of the repository.

2. Select the "Codespaces" tab and click "Create Codespace on main"

3. Once the browser based VS code environment loads, open the built-int terminal.

4. Type "python test_triangle.py" to run the triangle tests.

5. Type "python test_acceptance.py" to run the acceptance tests.

## Copilot Review Log

The following is a review of the changes made by Copilot in test_triangle.py and what I edited or accepted. 

| Test | Copilot suggested? | Kept / Edited / Rejected | Why |
|---|---|---|---|
| test_is_valid_triangle | Yes | Rejected | Original test included all different cases under one test. I separated them for proper testing. |
| test_is_invalid_triangle | Yes | Edited | This case was not created by Copilot. Originally it was part of one large test. |
| test_classify_equilateral_triangle | No | Edited | I created this case myself and used Copilot to scale this structure to the other tests. |
| test_classify_isosceles_triangle | No | Edited | Same as case above. |
| test_classify_scalene_triangle | No | Edited | Same as case above. |
| test_classify_right_scalene_triangle | No | Edited | Same as case above. |

### Final Thoughts

In testing I found that there did not need to be separate cases to determine if triangles were valid past the first case. Similarly, the original functions for classify_triangle must check equilateral before isosceles since the algorithm could mistake an isosceles for an equilateral. I placed the check for a right triangle after these initial cases to avoid missing the case or interfering with the output. 

Another note is that by definition, an equilateral triangle cannot be a right triangle since the right triangle can only have a maximum of two same length sides. 

The acceptance criteria I designed will determine if the glass is a proper triangle. If not then the test ends there. Once this is validated, the criteria determines if this is a right triangle or not and prompts the user to reinforce the edges if it is a right triangle.

#### A.I. Disclosure

In this project I utilized Copilot inline suggestions to create my initial test_triangle.py structure and edited the test cases to include more cases, remove redundancy, and expand existing cases. No other AI tool was used.
