#codewars.com/kata/5511b2f550906349a70004e1/python
def last_digit(n1, n2):
    n = pow(n1, n2, 10)
    return n % 10 if n % 2 == 0 else n % 10
