def transposeMatrix(matrix):
    rows=len(matrix)
    columns=len(matrix[0])
    trans_matrix=[]
    for i in range(columns):
        new_row=[]
        for j in range(rows):
            new_row.append(matrix[j][i])
        trans_matrix.append(new_row)
    return trans_matrix
