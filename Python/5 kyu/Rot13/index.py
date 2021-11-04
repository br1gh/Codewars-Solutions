#codewars.com/kata/530e15517bc88ac656000716/python
import string
def rot13(message):
    return message.encode("rot13")

#Alternative version
def rot131(message):
    a = 'nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM'
    b = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return ''.join([b[a.index(i)] if i in a else i for i in message])
