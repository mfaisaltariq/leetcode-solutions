def reverse(x: int) -> int:
    is_negative = False
    if x >= 0 and x < 10:
        return x
    if x < 0:
        is_negative = True
        x *= -1
        
    reversed_num = 0
    print(x)
    
    while x >= 10:
        reversed_num = reversed_num * 10 + (x % 10)
        x = x // 10
    
    reversed_num = (reversed_num * 10) + x
    if is_negative:
        reversed_num *= -1
    range_val = 2 ** 31
    if(reversed_num >= range_val -1 or reversed_num <= -range_val):
        return 0
    return reversed_num

print(reverse(1534236469))
print(2**31)