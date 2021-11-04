#codewars.com/kata/52774a314c2333f0a7000688/python
def valid_parentheses(string):
    if not string:
        return True
    else:
        return string.count('(') == string.count(')') and string[0] != ')' and string[-1] != '('
