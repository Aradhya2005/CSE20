def calculate(matrix, scalar):
    res = []
    for row in matrix:
        new_row = [element * scalar for element in row]
        res.append(new_row)
    return res


if __name__ == '__main__':
    scalar = 3
    A = [[1,0,0],[0,1,0],[0,0,1]]

    D = calculate(A, scalar)
    assert D == [[3,0,0], [0,3,0],[0,0,3]]
