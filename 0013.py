def romanToInt(s: str) -> int:
    value = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000}
    total = 0
    current_value = 0
    for symbol in s[::-1]:
        if value[symbol] >= current_value:
            current_value = value[symbol]
            total += value[symbol]
        else:
            total -= value[symbol]
    return total



if __name__ == "__main__":
    assert romanToInt("III") == 3
    assert romanToInt("LVIII") == 58
    assert romanToInt("MCMXCIV") == 1994