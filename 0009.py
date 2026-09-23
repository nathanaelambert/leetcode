def isPalindrome(x: int) -> bool:
    s = str(x)
    l, r = 0, len(s) - 1
    while 0 <= l <= r < len(s) and s[l] == s[r]:
        l += 1
        r -= 1
    return l >= r


if __name__ == "__main__":
    assert isPalindrome(121) is True
    assert isPalindrome(-121) is False
    assert isPalindrome(10) is False

