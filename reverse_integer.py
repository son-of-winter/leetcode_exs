def reverse(x: int) -> int:
    positive_x = abs(x)
    numbers = [char for char in str(positive_x)]
    reversed_numbers = numbers[::-1]
    result = "".join(reversed_numbers)
    if positive_x == x:
        return int(result) if 2147483648 > result > -2147483649 else 0
    else:
        return -int(result) if 2147483648 > result > -2147483649 else 0
    
"""
def reverse(self, x: int) -> int:
    negative = x < 0
    reverse = int(str(x)[(1 if negative else 0):][::-1])
    if negative: reverse = -reverse
    return reverse if 2147483648 > reverse > -2147483649 else 0
"""   

print(reverse(120))