#codewars.com/kata/55a29405bc7d2efaff00007c/python
def going(n):
    result,f = 1,1
    for i in range(2,n+1): f *= i; result += f
    return float(str(result/f)[:8])
