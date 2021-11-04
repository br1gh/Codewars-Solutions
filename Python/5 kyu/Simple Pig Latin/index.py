#codewars.com/kata/520b9d2ad5c005041100000f/python
def pig_it(text):
    text = text.split(' ')
    return ''.join([i[1:] + i[0] + 'ay ' if i.isalpha() else i + ' ' for i in text]).strip(' ')
