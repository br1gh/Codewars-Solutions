#codewars.com/kata/52742f58faf5485cae000b9a/python
def format_duration(seconds):
    sec,arr = seconds,[]
    for i in [[31536000,' years'],[86400,' days'],[3600,' hours'],[60,' minutes'],[1,' seconds']]:
        arr.append([sec//i[0],i[1]] if sec//i[0] != 1 else [sec//i[0],i[1][:-1]])
        sec -= arr[-1][0]*i[0]
    return ' and '.join((', '.join([str(i[0])+i[1] for i in arr if i[0]])).rsplit(', ',1)) if seconds else 'now' 
