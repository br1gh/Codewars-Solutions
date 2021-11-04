#codewars.com/kata/5282b48bb70058e4c4000fa7/python
def hex_string_to_RGB(x): 
    return dict(zip('rgb',[int(x[i:i+2],16) for i in range(1,6,2)]))
