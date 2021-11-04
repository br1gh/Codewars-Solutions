#codewars.com/kata/523d2e964680d1f749000135/python
import itertools as it
def interleave(*args):
    return [j for i in list(it.zip_longest(*args)) for j in i]

#Alternative version  
def interleave1(*args):
    return [j[i] if i < len(j) else None for i in range(len(max(args,key=len))) for j in args]
