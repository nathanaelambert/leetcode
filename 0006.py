def convert(s: str, numRows: int) -> str:
    rows = ["" for i in range(numRows)]

    def zigzag(index):
        max_row_id = numRows - 1
        if max_row_id == 0:
            return 0
        index = index % (2*max_row_id)
        if index > max_row_id:
            index = 2*max_row_id - index
        return index

    for i in range(len(s)):
        rows[zigzag(i)] += s[i]
    return "".join(rows)

if __name__ == "__main__":
    assert convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
    assert convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
    assert convert("A", 1) == "A"

