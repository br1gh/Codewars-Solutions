#codewars.com/kata/52190daefe9c702a460003dd/python
import regex as re
def search_substr(full_text, search_text, allow_overlap=True):
    return len([i for i in re.findall(search_text,full_text,overlapped=allow_overlap) if i])
