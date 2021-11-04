#codewars.com/kata/513e08acc600c94f01000001/python
def rgb(r, g, b):
    arr = [255 if i > 255 else 0 if i < 0 else i for i in [r,g,b]]
    return ''.join([format(i, '02x').upper() for i in arr])
