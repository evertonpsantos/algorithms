def is_palindrome_recursive(word, low_index, high_index):
    if word == '' or word is None:
        return False

    if high_index <= low_index:
        return True

    if word[high_index] != word[low_index]:
        return False

    return is_palindrome_recursive(word, low_index + 1, high_index - 1)
