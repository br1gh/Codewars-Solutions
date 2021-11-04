#codewars.com/kata/5270d0d18625160ada0000e4/python
def score(dice):
    score = sum([i*100 for i in range(7) if i in [2,3,4,6] and dice.count(i) >= 3])
    if dice.count(1) >= 3: score += 1000 + (dice.count(1)-3)*100
    else: score += dice.count(1)*100
    if dice.count(5) >= 3: score += 500 + (dice.count(5)-3)*50
    else: score += dice.count(5)*50
    return score
