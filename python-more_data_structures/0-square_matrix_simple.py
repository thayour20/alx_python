def square_matrix_simple(matrix=[]):
     squared_matrix = []
     for row in matrix:
          new_row = []
          for element in row:
               new_row.append(element ** 2)
          squared_matrix.append(new_row)
     return (squared_matrix)