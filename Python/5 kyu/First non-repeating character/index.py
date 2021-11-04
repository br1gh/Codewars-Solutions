#codewars.com/kata/52bc74d4ac05d0945d00054e/python
def first_non_repeating_letter(s):
    try: return [i for i in s if s.lower().count(i.lower()) == 1][0]
    except: return ''
