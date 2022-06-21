from typing import List
def encode(strs: List) -> str:
    return ''.join(
        f'{len(string)}#{string}'
        for string in strs
    )

def decode(str: str) -> List:
    res, i = [], 0

    while i < len(str):
        j = i

        while str[j] != '#':
            j+=1
        length = int(str[i:j])
        res.append(str[j+1: j+1+length])
        i = j + 1 + length

    return res


print(encode(["my", "name", "2#", "faisal"]))
print(decode("2#my4#name2##26#faisal"))