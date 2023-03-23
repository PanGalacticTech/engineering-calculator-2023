

def return_rows_columns(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    #print(f"Rows: {rows}, Columns: {columns}")
    return [rows, columns]


def print_rows_columns(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    print(f"Rows: {rows}, Columns: {columns}")
    return [rows, columns]


def print_matrix(matrix):
    #return_rows_columns(matrix)
    for i in matrix:
        print(i)
    return matrix




def return_n_row(matrix, n):
    row_list = []
    rows_columns = return_rows_columns(matrix)
    if n > rows_columns[0]:
        print("Index Out of Bounds")
    else:
        #print(matrix[n])
        return matrix[n]


def return_n_column(matrix, n):
    column_list = []
    rows_columns = return_rows_columns(matrix)
    if n > rows_columns[1]:
        print("Index Out of Bounds")
    else:
        for i in matrix:
            column_list.append(i[n])
            #print(i[n])
        #print(column_list)
        return column_list

# For 2x2 matrixes. Only used once already tested so does not need to test
def split_matrix(matrix):
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    d = matrix[1][1]
    matrix_dic = {
        "a": a,
        "b": b,
        "c": c,
        "d": d
    }
    return matrix_dic


# Only valid for 2x2 matrices
def return_determinant(matrix):
    rows_columns = return_rows_columns(matrix)
    if rows_columns[0] == 2 and rows_columns[1] == 2:
        split = split_matrix(matrix)
        determinant = split["a"]*split["d"] - split["b"]*split["c"]
        print(f"Determinant: {determinant}")
        return determinant
    else:
        print("Matrix size is not 2x2")

def print_inverted_mx(matrix, determinant):
    print(f"1/{determinant}")
    for i in matrix:
        print(i)
    return matrix


# Only valid for 2x2 matrices
def invert_matrix(matrix):
    print("Invert Matrix")
    print_matrix(matrix)
    determinant = return_determinant(matrix)
    split = split_matrix(matrix)
    inverted_matrix = [[split["d"],-1*split["b"]],
                       [-1*split["c"],split["a"]]]
    print_inverted_mx(inverted_matrix, determinant)
    i = 0
    for row in inverted_matrix:
        j = 0
        #print(f"row: {row}")
        for item in row:
            #print(f"item: {item}  /   determinant: {determinant}")
            new_item = item/determinant
            #print(f"New Item: {new_item}")
            inverted_matrix[i][j] = new_item
            j =+ 1
        i =+ 1
    print_matrix(inverted_matrix)
    return inverted_matrix

def matrix_dot_matrix(A, B):
    print("Matrix Multiplication")
    rows_columns_A = print_rows_columns(A)
    rows_columns_B = print_rows_columns(B)
    if rows_columns_A[1] == rows_columns_B[0]:
        product = []
        print("Matrix: A")
        print_matrix(A)
        print("Matrix: B")
        print_matrix(B)
        for i in range(rows_columns_A[0]):
            row_out = []
            row_A = return_n_row(A, i)
            print(f" Row_A: {row_A}")
            for k in range(rows_columns_B[1]):
                column_B = return_n_column(B, k)
                print(f" column_B: {column_B}")
                value = 0
                for j in range(rows_columns_A[1]):
                    value = value + row_A[j] * column_B[j]
                row_out.append(value)
            product.append(row_out)
        print_matrix(product)
        return product







        # do calculation
    else:
        print("Matrices are Incompatable for Multiplication")




