#codewars.com/kata/550f22f4d758534c1100025a/python
def dirReduc(arr):
    x = [['NORTH', 'SOUTH'], ['SOUTH', 'NORTH'], ['EAST', 'WEST'], ['WEST', 'EAST']]
    while True:
        for i in range(len(arr)-1):
            if [arr[i], arr[i+1]] in x:
                arr = arr[:i] + arr[i+2:]
                break
        else: break
    return arr
