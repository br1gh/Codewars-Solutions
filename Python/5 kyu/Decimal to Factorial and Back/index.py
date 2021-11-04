#codewars.com/kata/54e320dcebe1e583250008fd/python
base = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def dec2FactString(nb):
    s, div = '', 1
    while nb // div != 0:
        s += base[nb % div]
        nb //= div
        div += 1
    return (s + base[nb % div])[::-1]

def factString2Dec(string):
    arr = [1]
    for i in range(1,len(string)): arr.append(arr[-1]*i)
    return sum([base.index(i)*j for i,j in zip(string[::-1],arr)])
