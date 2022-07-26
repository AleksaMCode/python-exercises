def rectangle_draw(size: int, symbol="#"):
    """
    Prints a hollow rectangle pattern of symbols.
    :param size: Size of the drawn rectangle
    :param symbol: Symbol used as a rectangle pattern
    :return: False if the pattern size isn't in the limit
    """
    if size < 3 or size > 100:
        return False

    for i in range(0, size - 1):
        print()
        for j in range(0, size):
            if j == 0 or j == size - 1 or i == 0 or i == size - 2:
                print(symbol, end='')
            else:
                print(" ", end='')

    return True


def square_draw(size: int, symbol: str = "#") -> bool:
    """
    Prints a hollow square pattern of symbols.
    :param size: Size of the drawn square
    :param symbol: Symbol used as a rectangle pattern
    :return: False if the pattern size isn't in the limit
    """
    if size < 2 or size > 100:
        return False

    for i in range(0, size):
        print()
        for j in range(0, size):
            if j == 0 or j == size - 1 or i == 0 or i == size - 1:
                print(symbol, end='')
            else:
                print(" ", end='')

    return True
