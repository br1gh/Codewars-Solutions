#codewars.com/kata/514a024011ea4fb54200004b/python
import re
def domain_name(url):
    return re.sub('www.|http://|https://','',url).split('.')[0]
