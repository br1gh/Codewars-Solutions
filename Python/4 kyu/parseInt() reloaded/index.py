#codewars.com/kata/525c7c5ab6aecef16e0001a5/python
import re
def parse_int(string):
    nums, x = {
        'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,
        'nine':9,'ten':10,'eleven':11,'twelve':12,'thirteen':13,'fourteen':14,'fifteen':15,
        'sixteen':16,'seventeen':17,'eighteen':18,'nineteen':19,'twenty':20,
        'thirty':30,'forty':40,'fifty':50,'sixty':60,'seventy':70,'eighty':80,'ninety':90,
        'zero':0,'hundred':100,'thousand':1000,'million':1000000}, []
    for i in [nums[i] for i in re.split(' and |-| ',string)]:
        if i in [100,1000000]: x[-1] *= i
        else: x.append(i)
    return sum([sum(x[:x.index(1000)])*1000,sum(x[x.index(1000)+1:])]) if 1000 in x else sum(x)
