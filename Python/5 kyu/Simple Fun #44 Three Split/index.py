#codewars.com/kata/588833be1418face580000d8/python
def three_split(a):
    count = 0
    for i in range(1,len(a)-1):  
        if 2*sum(a[:i]) == sum(a[i:]):
            for j in range(1,len(a)-i): 
                if sum(a[i:i+j]) == sum(a[i+j:]): count += 1
    return count
