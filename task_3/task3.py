def palindrome_check1(word):
    """
    Checks if a word is a palindrome.
    :param word: String used to check if it's palindrome.
    :return: True if the word is palindrome, otherwise False.
    """
    rev_word = word[::-1]
    return rev_word == word


def palindrome_check2(word):
    """
    Checks if a word is a palindrome.
    :param word: String used to check if it's palindrome.
    :return: True if the word is palindrome, otherwise False.
    """
    n = len(word)
    for i in range(n):
        if word[i] != word[n - (i + 1)]:
            return False
    return True
