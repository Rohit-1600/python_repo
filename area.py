def calculate_rectangle_area(length, width):
    """
    Calculate the area of a rectangle.

    Args:
    length (float): The length of the rectangle.
    width (float): The width of the rectangle.

    Returns:
    float: The area of the rectangle.
    """
    area = length * width
    return area

# Example usage
length = 5
width = 3
print("Length:", length)
print("Width:", width)
print("Area of rectangle:", calculate_rectangle_area(length, width))
