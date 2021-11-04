#codewars.com/kata/53db96041f1a7d32dc0004d2/python
import numpy as n
def done_or_not(arr):
    col = [[i[j] for i in arr] for j in range(9)]
    blocks = n.array(n.array(arr).reshape((3,3,3,3)).transpose((0,2,1,3)).reshape((9,9))).tolist()
    result = all(sorted(i) == [i for i in range(1,10)] for i in blocks) and all(sorted(i) == [i for i in range(1,10)] for i in col)
    return 'Finished!' if result else 'Try again!'
