#codewars.com/kata/56882731514ec3ec3d000009/python
four = [4*["Yellow"], 4*["Red"]]
def who_is_winner(pieces_position_list):
    grid = [7*[0] for i in range(6)]
    arr = [[ord(i[0])-65, i[2:]] for i in pieces_position_list]
    for i in arr:
        row = 5 
        while row >= 0 and grid[row][i[0]] != 0:
            row -= 1
        grid[row][i[0]] = i[1]
        if check(grid):
            return i[1]
    return "Draw"
        
def check(arr):
    for i in range(6):
        for j in range(4):
            if arr[i][j:j+4] in four:
                return 1
                
    for i in range(3):
        for j in range(7):
            if [arr[i][j], arr[i+1][j], arr[i+2][j], arr[i+3][j]] in four:
                return 1
    
    for i in range(3):
        for j in range(4):
            if [arr[i][j], arr[i+1][j+1], arr[i+2][j+2], arr[i+3][j+3]] in four:
                return 1
    
    for i in range(3):
        for j in range(3,7):
            if [arr[i][j], arr[i+1][j-1], arr[i+2][j-2], arr[i+3][j-3]] in four:
                return 1
