def reverse_string(input_string):
    """
    Reverse a given string.

    Args:
    input_string (str): The string to be reversed.

    Returns:
    str: The reversed string.
    """
    return input_string[::-1]

# Example usage
input_str = "Hello, World!"
print("Original string:", input_str)
print("Reversed string:", reverse_string(input_str))
