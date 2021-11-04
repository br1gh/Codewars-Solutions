#codewars.com/kata/526989a41034285187000de4/python
def ips_between(start, end):
    arr = [int(j)-int(i) for i,j in zip(start.split('.'),end.split('.'))]
    return sum([x*y for x,y in zip(arr,[256**i for i in range(3,-1,-1)])])
