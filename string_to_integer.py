def myAtoi(s: str) -> int:
    s = s.lstrip()
    if not s:
        return 0

    sign = 1
    index = 0

    if s[0] == '+':
        index += 1
    elif s[0] == '-':
        sign = -1
        index += 1

    result = 0
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31

    while index < len(s) and s[index].isdigit():
        digit = int(s[index])

        if result > INT_MAX // 10 or (result == INT_MAX // 10 and digit > INT_MAX % 10):
            return INT_MAX if sign == 1 else INT_MIN

        result = result * 10 + digit
        index += 1

    return sign * result

print(myAtoi(" -042"))