#codewars.com/kata/52449b062fb80683ec000024/python
def generate_hashtag(s):
    s = '#' + ''.join([i.title() for i in s.split(' ')])
    return s if len(s) in range(2,141) else 0
