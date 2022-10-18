def check_for_seats(matrix):
    l = []
    for column in range(0, len(matrix[1])):
        for row in range(len(matrix)-1, -1, -1):
            element = matrix[row][column]
            # print("OK")
            # print(element)
            # print("OK")
            for r in range(row-1, -1, -1):
                # print(matrix[r][column])
                if matrix[r][column] >= element:
                    l.append((row, column))

    return l


A = [[1, 2, 3, 2, 1, 1],
     [2, 4, 4, 3, 7, 2],
     [5, 5, 2, 5, 6, 4],
     [6, 6, 7, 6, 7, 5]]

print(check_for_seats(A))
