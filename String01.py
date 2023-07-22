def main(s):
    """
    A str of several words is given. All letters are lowercase. Make sure that the first letter of each word is capitalized.
    Args:
        s: str
    Returns:
        str: answer
    """
    s="google is a search engine"
    return s.title()
print(main("google is a search engine"))