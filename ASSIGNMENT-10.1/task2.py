#refactor the code with google style doc string with type hints
def area_of_rect(L,B):return L*B
print(area_of_rect(10,20))
def area_of_rect(L: float, B: float) -> float:
    """Calculate the area of a rectangle.

    Args:
        L (float): The length of the rectangle.
        B (float): The breadth of the rectangle.

    Returns:
        float: The area of the rectangle.
    """
    return L * B

print(area_of_rect(10, 20))
