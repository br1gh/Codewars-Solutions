#codewars.com/kata/525caa5c1bf619d28c000335/python
def isSolved(b):
    arr = list(map(list, zip(*b))) + [[b[i][i] for i in range(3)]] + [[b[0][2],b[1][1],b[2][0]]] + b
    if [1,1,1] in arr: return 1
    if [2,2,2] in arr: return 2
    else: return -1 if 0 in [i for j in arr for i in j] else 0

#Alternative version 
def isSolved(b):
    arr = list(map(list, zip(*b))) + [[b[i][i] for i in range(3)]] + [[b[0][2],b[1][1],b[2][0]]] + b
    return 1 if [1,1,1] in arr else 2 if [2,2,2] in arr else (-1 if 0 in [i for j in arr for i in j] else 0)
