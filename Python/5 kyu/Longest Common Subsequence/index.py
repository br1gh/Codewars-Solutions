#codewars.com/kata/52756e5ad454534f220001ef/python
import itertools as it
def comb(z):
    return [''.join(k) for j in [list(it.combinations(z,i)) for i in range(1,len(z)+1)] for k in j]
def lcs(x, y):
    try: return sorted(list(set(comb(x)) & set(comb(y))),key=len)[-1]
    except: return ''
