def main(s):
    """
    A variable of type str is given. make sure all letters are lowercase.
    Args:
        s: str
    Returns:
        bool: answer
    """
    s="Python"
    if s.lower():
        return True
    else:
        return False
print(main("Python"))