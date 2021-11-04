#codewars.com/kata/55983863da40caa2c900004e/python
def next_bigger(n):
    for i in range(n+1, int(''.join(sorted(str(n))[::-1]))+1):
        if sorted(str(i))[::-1] == sorted(str(n))[::-1]: return i; break
    return -1
