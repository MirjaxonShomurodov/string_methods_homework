def main(s):
    """
    A variable of type str is given. Make sure it only consists of uppercase letters.
    Args:
        s: str
    Returns:
        bool: answer
    """
    if s.upper():
        return True
    else:
        return False 
print(main("hello"))