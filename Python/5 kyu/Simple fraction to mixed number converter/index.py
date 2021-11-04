#codewars.com/kata/556b85b433fb5e899200003f/python
from fractions import Fraction
def mixed_fraction(s):
    out = ''
    arr = []
    s = [int(i) for i in s.split('/')]
    arr.append(int(s[0]/s[1]))
    arr.append(s[0]-int(s[0]/s[1])*s[1])
    arr.append(s[1])
    if arr[0] != 0:
        out = str(arr[0]) + ' ' + str(abs(Fraction(arr[1],arr[2])))
    else:
        out = str(Fraction(arr[1],arr[2]))
    if '0 ' in out:
        out = out[3:]
    if ' 0' in out:
        out = out[:-2]
    return out
