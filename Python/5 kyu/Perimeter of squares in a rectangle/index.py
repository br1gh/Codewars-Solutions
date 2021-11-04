#codewars.com/kata/559a28007caad2ac4e000083/python
def perimeter(n):
    arr = [1,1]
    for i in range(n-1): arr.append(arr[-1] + arr[-2])
    return 4*sum(arr)
