def is_palindrome_not_recursive(word):
    for i in range(len(word) // 2):
        if word[i] != word[-1 - i]:
            return False
    return True


def is_palindrome(word):  # Rekursiv
    if len(word) <= 1:
        return True

    if word[0] != word[-1]:
        return False

    return is_palindrome(word[1:-1])


assert is_palindrome("racecar")
assert not is_palindrome("etwas")
