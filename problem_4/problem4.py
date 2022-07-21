def strcmp(first: str, second: str):
    if first == second:
        return 0
    if len(first) != len(second):
        return 0 if first == second else (-1 if len(first) > len(second) else 1)
    else:
        for i, j in zip(range(0, len(first)), range(0, len(second))):
            if first[i] != second[j]:
                return -1 if first[i] > second[j] else 1
