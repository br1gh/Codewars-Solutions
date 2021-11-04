#codewars.com/kata/526dbd6c8c0eb53254000110/python
import re
def alphanumeric(string):
    return bool(re.match("^[a-zA-Z0-9]*$", string))

#Alternative version  
def alphanumeric1(string):
    return string.isalnum()
