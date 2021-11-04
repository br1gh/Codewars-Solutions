#codewars.com/kata/529bf0e9bdf7657179000008/python
def validSolution(arr):
    x = [arr[j][i:i+3]+arr[j+1][i:i+3]+arr[j+2][i:i+3] for i in range(0,9,3) for j in range(0,9,3)]
    return [sorted([i[j] for i in arr]) for j in range(9)] == [sorted(i) for i in x]
