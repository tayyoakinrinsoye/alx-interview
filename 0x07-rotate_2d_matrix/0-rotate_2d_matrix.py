def rotate_2d_matrix(matrix):
    """
    Rotate an n x n 2D matrix 90 degrees clockwise in-place.

    :param matrix: The input 2D matrix to rotate.
    :type matrix: List[List[int]]
    """
    n = len(matrix)

    # Step 1: Transpose the matrix in-place
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row of the transposed matrix in-place
    for i in range(n):
        matrix[i].reverse()

