#codewars.com/kata/51edd51599a189fe7f000015/python
def solution(a, b):
    return sum([abs(i-j)**2 for i,j in zip(a,b)])/len(a)
