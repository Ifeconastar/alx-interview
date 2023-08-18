#!/usr/bin/python3

def rotate_2d_matrix(matrix):
    """
    Rotate the given n x n 2D matrix 90 degrees clockwise in-place.

    Args:
    matrix (List[List[int]]): The input 2D matrix to be rotated.

    Returns:
    None: The matrix is modified in-place.
    """
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row to complete the rotation
    for i in range(n):
        matrix[i] = matrix[i][::-1]

# Example usage
if __name__ == "__main__":

    input_matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print("Original Matrix:")
    for row in input_matrix:
        print(row)

    rotate_2d_matrix(input_matrix)

    print("\nRotated Matrix:")
    for row in input_matrix:
        print(row)
