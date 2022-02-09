"""
The easy way is to move top to bottom and when bottom is reached reverse the movement
this way we can easily form the rows and then join them at the end

but the complexity for this is n+m and space complexity is also numRows
"""
def convert2(s: str, numRows: int) -> str:
    if len(s) == 1 or numRows <= 1:
        return s

    arr = [[] for x in range(numRows)]
    row = 0
    down = True
    for i,char in enumerate(s):
        
        arr[row].append(char)

        if row == 0:
            down = True
        elif row == numRows -1:
            down = False

        if down:
            row += 1
        else:
            row -= 1
    res = ""
    for r in range(numRows):
        res += "".join(arr[r])
    return res


"""
A better way to do things is to jump values and go to the next char that would be on the same row 
to get to the next char on same row we can simply 2 * (numRows - 1) calculate it this way.

But this works only in the case for the first and last row, for all other rows there are intermediate
characters and in order to capture them we do another calculation that is 
current index i + increment - 2 * current row num

time complexity is 0(n)
space complexity is 0(1)
"""

def convert(s: str, numRows: int) -> str:
    if numRows <= 1: return s

    res = ""
    counter = 0
    for r in range(numRows):
        increment = 2 * (numRows -1)
        counter += 1
        print(counter, 'c')
        for i in range(r, len(s), increment):
            counter += 1
            print(counter, 'c inside', s[i])
            res += s[i]
            if (r > 0 and r < numRows - 1 and i + increment - (2*r) < len(s)):
                print(s[i + increment - 2 * r])
                res += s[i + increment - 2 * r]

    return res



# print(zigZagConcat("PAYPALISHIRING", 3))
print(convert2("PAYPALISHIRING", 3))

# P A Y P A L I S H I R  I  N  G
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13


# PAHN 2 * n - 2
# APLSIIG 2 * (n-rowNum) - 2
# YIR     2 * (n) - 2

# PAHN
# ALIG
# YIR
# PSI