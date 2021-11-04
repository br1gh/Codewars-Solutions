#codewars.com/kata/52597aa56021e91c93000cb0/python
def move_zeros(array):
    end, c = [], 0
    for i in array:
        if type(i) != bool:
            if i != 0: end.append(i)
            else: c += 1
        else: end.append(i)
    return end + c*[0]
