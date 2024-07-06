def get_matrix(n, m, value):
    matrix = []
    for line in range(n):
        line_list = []
        for column in range(m):
            line_list.append(value)
        matrix.append(line_list)
    print(matrix)
get_matrix(3,5,42)
get_matrix(4,6,41)
get_matrix(1,7,44)
get_matrix(3,9,47)
get_matrix(7,9,45)












