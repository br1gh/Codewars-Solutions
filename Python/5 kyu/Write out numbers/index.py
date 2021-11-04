#codewars.com/kata/52724507b149fa120600031d/python
def t(n):
    d = {0:'',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',
    10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',
    17:'seventeen',18:'eighteen',19:'nineteen',20:'twenty',30:'thirty',40:'forty',50:'fifty',
    60:'sixty',70:'seventy',80:'eighty',90:'ninety'}
    n = str(n)
    w = d[int(n[-2:])] if int(n[-2:]) in d else d[int(n[-2])*10]+'-'+d[int(n[-1])] if len(n)>1 else d[int(n[0])]
    return w if len(n) < 3 else d[int(n[0])] + ' hundred ' + w
def number2words(n):
    output = t(n//1000)+' thousand '+t(n%1000) if n > 999 else t(n%1000)
    return 'zero' if n == 0 else output.strip()
