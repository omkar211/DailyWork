#Code
def valid(A,col,row,key):
    for i in range(10):
        # for col
        if(A[i][col]==key):
            return False
        # for row
        if A[row][i]==key:
            return False
        # for grid 
        for i in range():
            for j in range():
                if(A[i][j]==key):
                    return False
    return True
def suduko(A,col,row):
    if row>9:
        return True
     if A[row][col]!=-1:
            col+=1
            if col==9:
                row+=1
                col=0
            return suduko(A)
    for i in range(10):
        if(valid(A,row,col,i)):
            A[row][col]=i
            col+=1
            if(col==9):
                col=0
                row+=1
            is_placed=suduko(A,col,row)
            if is_placed:
                return True
            col-=1
            if col==-1:
                row-=1
                col=8
    return False


