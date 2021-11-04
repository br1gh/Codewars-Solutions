#codewars.com/kata/51ba717bb08c1cd60f00002f/python
def solution(args):
    arr,ren = [],[]
    for i in args:
        if not ren or i-1 == int(ren[-1]): ren.append(str(i))
        else:
            arr.append(ren)
            ren = [] 
            ren.append(str(i))
    return ','.join([i[0]+'-'+i[-1] if len(i)>2 else ','.join(i) for i in arr + [ren]])
