import math


def solution(s):
    str = ""
    z = len(s) / 2
    t = math.ceil(z)
    res = [None] * t
    j = 0
    for i in range(len(s)):
        str += s[i]
        if i == len(s) - 1 and len(s) % 2 != 0:
            res[j] = str + "_"
        if i % 2 != 0:
            res[j] = str
            str = ""
            j += 1
    return res
