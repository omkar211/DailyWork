
#Code
def valid(col,row,grid):
    #row
    for i in range(row):
        if grid[i][col]:
            return false
    #col
    for i in range(col):
        if grid[row][i]:
            return False
    #Primary diagnol
    for i in range(row,-1,-1):
        for j in range(col,-1,-1):
            if grid[i][j]:
                return False

    #Secondary diagnol
    for i in range(row,-1,-1):
        for j in range(col,len(grid[0])):
            if grid[i][j]:
                return False
    return True


def queen(grid,row):
    if row>=len(grid):
        return True
    for col in range(len(grid[0])):
        if(valid(col,row,grid)):
            grid[row][col]=True
            flag=queen(grid,row+1)
            if flag:
                return flag
            grid[row][col]=False
    return false


#Code
def valid2(row,col,placed):
    for i in range(row):
        if(placed[i]==col):
            return False
        if i-placed[i]==row-col:
            return False
        if i+placed[i]==row+col:
            return False
    return False
def queen2(row,placed):
    if row>=len(placed):
        return True
    for col in range(len(placed)):
        if not valid2(row,col,placed):
            continue
        placed[row]=col
        flag=queen(row+1,placed)
        if flag:
            return flag
        placed[row]=0
    return False

#Code3
def queen3(row,placed,primary_diagnol,secondary_diagnol,col_placed):
    if row>=len(placed):
        return True
    for col in range(len(placed)):
        if col_placed[col] or primary_diagnol[row+col] or secondary_diagnol[row-col+len(placed)-1]:
            continue
        col_placed[col]=True
        primary_diagnol[row+col]=True
        secondary_diagnol[row-col+len(placed)-1]=True
        flag=queen3(row+1,placed,primary_diagnol,secondary_diagnol,col_placed)
        if flag:
            return flag
        
        col_placed[col]=False
        primary_diagnol[row+col]=False
        secondary_diagnol[row-col+len(placed)-1]=False
    return False        