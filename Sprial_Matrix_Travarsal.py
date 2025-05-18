"""
3. Spiral Matrix Traversal (Hard)
a. Description: Return elements of an m x n matrix in spiral order using
nested for loops.
b. Example: Input: matrix = [[1,2,3],[4,5,6],[7,8,9]] → Output:
[1,2,3,6,9,8,7,4,5]
c. Relevance: Tests complex loop logic and boundary handling.
"""
def spiralOrder(matrix):
    if not matrix:
        return []
    result = []
    row_start, row_end = 0, len(matrix) - 1
    col_start, col_end = 0, len(matrix[0]) - 1
    while row_start <= row_end and col_start <= col_end:
        for i in range(col_start, col_end + 1):
            result.append(matrix[row_start][i])
        row_start += 1
        for i in range(row_start, row_end + 1):
            result.append(matrix[i][col_end])
        col_end -= 1
        if row_start <= row_end:
            for i in range(col_end, col_start - 1, -1):
                result.append(matrix[row_end][i])
            row_end -= 1
        if col_start <= col_end:
            for i in range(row_end, row_start - 1, -1):
                result.append(matrix[i][col_start])
            col_start += 1
    return result
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(spiralOrder(matrix))