def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> `valid_parentheses("(()())")`
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    count = 0

    for par in parens:
        if par == '(':
            count += 1
        elif par == ')':
            count -= 1

        if count < 0:
            return False
    return count == 0