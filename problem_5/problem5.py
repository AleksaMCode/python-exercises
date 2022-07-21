def rectangle_draw(size: int, symbol: str = "#"):
    for i in range(0, size - 1):
        print()
        for j in range(0, size):
            if j == 0 or j == size - 1 or i == 0 or i == size - 2:
                print(symbol, end='')
            else:
                print(" ", end='')


def square_draw(size: int, symbol: str = "#"):
    for i in range(0, size):
        print()
        for j in range(0, size):
            if j == 0 or j == size - 1 or i == 0 or i == size - 1:
                print(symbol, end='')
            else:
                print(" ", end='')
