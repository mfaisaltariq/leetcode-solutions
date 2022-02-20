def myAtoi(s: str) -> int:
    is_negative = False
    s = s.strip()

    if (s[0] == '-'):
        is_negative = True
        s = s[1:]
    elif(s[0] == '+'):
        s = s[1:]
    num = 0
    for i,v in enumerate(s):
        if (v >= '0' and v <= '9'):
            num = num * 10 + int(v)
        else:
            break

    if is_negative:
        num *= -1

    range = 2 ** 31
    if num < -range:
        return -range
    elif num > range -1:
        return range -1

    return num

print(myAtoi("-100de"))
print(myAtoi("9203"))
print(myAtoi("-67400 de"))
        