A = [[2,3],[5,8]]
B = [[1,4],[8,6]]

def addMatrices(a,b):
    '''adds two 2x2 matrices together'''
    C = [[a[0][0]+b[0][0],a[0][1]+b[0][1]],
    [a[1][0]+b[1][0],a[1][1]+b[1][1]]]
    return C

def multmatrix(a,b):
    #Returns the product of matrix a and matrix b
    m = len(a) #number of rows in first matrix
    n = len(b[0]) #number of columns in second matrix
    newmatrix = []
    for i in range(m):
        row = []
        #for every column in b
        for j in range(n):
            sum1 = 0
            #for every element in the column
            for k in range(len(b)):
                sum1 += a[i][k]*b[k][j]
            row.append(sum1)
        newmatrix.append(row)
    return newmatrix

C = addMatrices(A,B)
print(C)
