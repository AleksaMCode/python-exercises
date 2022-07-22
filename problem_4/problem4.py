def strcmp(first, second):
    """
    Compares two strings lexicographically.
    :param first: String to be compared.
    :param second: String to be compared.
    :return: 0 if the contents of both strings are equal, <0 if the first character that does not match
    has a greater value in ptr1 than in ptr2 and >0 if the first character that does not match has a lower
    value in ptr1 than in ptr2
    """
    if first == second:
        return 0
    elif len(first) != len(second):
        return -1 if len(first) > len(second) else 1
    else:
        for i, j in zip(range(0, len(first)), range(0, len(second))):
            if first[i] != second[j]:
                return -1 if first[i] > second[j] else 1
