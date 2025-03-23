def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s
    rows = [""] * numRows
    row_index = 0
    direction = 1  # 1 for downwards, -1 for upwards
    for char in s:
        rows[row_index] += char
        if row_index == 0:
            direction = 1  # Go downwards
        elif row_index == numRows - 1:
            direction = -1  # Go upwards
        row_index += direction
    return "".join(rows)