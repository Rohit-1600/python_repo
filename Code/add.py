def sum_of_elements(arr):
    """
    Calculate the sum of elements in the given array.

    Args:
    arr (list): The input array.

    Returns:
    int: The sum of elements in the array.
    """
    total = 0
    for num in arr:
        total += num
    return total

# Example usage
array = [1, 2, 3, 4, 5]
print("Array:", array)
print("Sum of elements:", sum_of_elements(array))
