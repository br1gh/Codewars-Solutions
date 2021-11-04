#codewars.com/kata/52f787eb172a8b4ae1000a34/python
import math
def zeros(n):
    return 0 if not n else sum([int(n/5**i) for i in range(1,int(math.log(n,5))+1)])
