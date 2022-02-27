'''
Reverse loop through roman values from largest to smallest and add the symbol to the final string.

The final string need to be added multiple times if the integer result for dividing num by roman symbol
is greater than 1 

repeat = num // value of symbol
'''

def intToRoman(num: int) -> str:
    dict = [
        ["I", 1],
        ["IV", 4],
        ["V", 5],
        ["IX", 9],
        ["X", 10],
        ["XL", 40],
        ["L", 50],
        ["XC", 90],
        ["C", 100],
        ["CD", 400],
        ["D", 500],
        ["CM", 900],
        ["M", 1000],
    ]
    res = ""
    for sym, val in reversed(dict):
        if num // val:
            repeat = num // val
            res += (sym * repeat)
            num %= val

    return res

print(intToRoman(58))