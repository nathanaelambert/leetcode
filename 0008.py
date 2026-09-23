import re


def myAtoi(s: str) -> int:
    s = s.lstrip()
    neg = s[0] == '-'
    s = s[1:] if s[0] == '-' or s[0] == '+' else s
    s.lstrip("0")
    match = re.match(r'\d+', s)
    number = int(match.group()) if match else 0
    number = number*(-1) if neg else number
    return min(2**31 -1, max(-2**31, number))




if __name__ == "__main__":
    assert myAtoi("42") == 42
    assert myAtoi("-42") == -42
    assert myAtoi("1337c0d3") == 1337
    assert myAtoi("0-1") == 0
    assert myAtoi("words and 987") == 0

