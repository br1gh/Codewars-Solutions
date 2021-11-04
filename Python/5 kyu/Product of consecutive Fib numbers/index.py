#codewars.com/kata/5541f58a944b85ce6d00006a/python
def productFib(prod):
    arr = [0, 1]
    while arr[-2] * arr[-1] < prod: arr.append(arr[-2] + arr[-1])
    return [arr[-2], arr[-1], arr[-2] * arr[-1] == prod] 
