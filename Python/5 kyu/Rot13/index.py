#codewars.com/kata/530e15517bc88ac656000716/python
def rot13(message):
    a = 'nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM'
    b = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return ''.join([b[a.index(i)] if i in a else i for i in message])
