def reverse_string(string):
    """Reverses a string
    Returns string"""
    reversed = ""
    for letter in string:
        reversed = letter + reversed
    return reversed

print reverse_string("ABCDEFGHIJKLMNOPQRSTUVWXYZ")