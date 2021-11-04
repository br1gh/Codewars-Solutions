#codewars.com/kata/529b418d533b76924600085d/python
import re
def to_underscore(string):
    return '_'.join([i.lower() for i in re.sub( r"([A-Z])", r" \1", str(string)).split()])
