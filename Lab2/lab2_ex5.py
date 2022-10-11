def relplaceMatrix(matrix, n, m):
    for i in range(0 , n):
        for j in range(0 , m):
            if i > j: # sub diagonal matrix
                matrix[i][j] = 0
    return matrix



A = [[1, 4, 5, 12], 
    [-5, 8, 9, 0],
    [-6, 7, 11, 19],
    [-1, 2, 14, 29]]

print(relplaceMatrix(A, 4, 4))