#codewars.com/kata/525a566985a9a47bc8000670/python
def rotate(matrix, direction): 
    x, y = len(matrix[0]), len(matrix)
    if direction == "clockwise":
        return [[matrix[y-j-1][i] for j in range(y)] for i in range(x)]
    else:
        return [[matrix[j][x-i-1] for j in range(y)] for i in range(x)]
