def myAtoi(s: str) -> int:
    s = s.lstrip()
    if not s: return 0
    neg = s[0] == '-'
    s = s[1:] if s[0] == '-' or s[0] == '+' else s
    s.lstrip("0")

    i = 0
    number = 0
    while i < len(s) and s[i].isdigit():
        number += int(s[i])
        number *= 10
        i += 1

    number = number // 10 *(-1) if neg else number // 10 
    return min(2**31 -1, max(-2**31, number))

if __name__ == "__main__":
    assert myAtoi("42") == 42
    assert myAtoi("-42") == -42
    assert myAtoi("1337c0d3") == 1337
    assert myAtoi("0-1") == 0
    assert myAtoi("words and 987") == 0

