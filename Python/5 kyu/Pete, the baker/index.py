#codewars.com/kata/525c65e51bf619685c000059/python
def cakes(r, a): 
    try: return min([a[k]/v for k, v in r.items()])
    except: return 0

#Alternative version 
def cakes1(r, a):
    return 0 if not all(i in a for i in r) else min([a[k]/v for k, v in r.items()]) 
