#codewars.com/kata/55c6126177c9441a570000cc/python
def order_weight(st):
    return ' '.join(sorted(st.split(), key=lambda x: (sum(map(int, x)), x)))
