def reverse(x: int) -> int:
    neg = x < 0
    x = x*(-1) if neg else x
    s = ""
    while(x > 0):
        digit = x % 10
        s += str(digit)
        x -= digit
        x = x // 10
    rev = int(s) if s else 0
    val = rev * -1 if neg else rev 
    return 0 if val.bit_length() > 31 else val

if __name__ == "__main__":
    assert reverse(123) == 321
    assert reverse(-123) == -321
    assert reverse(120) == 21
        