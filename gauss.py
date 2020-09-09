def gauss(A):
    m = len(A)
    n = len(A[0])
    
    for j, row in enumerate(A):
        if row[j] != 0:
            divisor = row[j]
            for i, term in enumerate(row):
                row[i] = term / divisor

        for i in range(m):
            if i != j:
                addinv = -1*A[i][j]

                for ind in range(n):
                    A[i][ind] += addinv*A[j][ind]
    return A

B = [[2,-1,5,1,-3],
[3,2,2,-6,-32],
[1,3,3,-1,-47],
[5,-2,-3,3,49]]
print(gauss(B))
