#codewars.com/kata/52e88b39ffb6ac53a400022e/python
def int32_to_ip(int32):
    return '.'.join([str((int32%256**i)//256**(i-1)) for i in range(4,0,-1)])
