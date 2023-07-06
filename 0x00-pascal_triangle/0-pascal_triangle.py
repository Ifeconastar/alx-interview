#!/usr/bin/python3
"""Pascal Triangle"""


def pascal_triangle(n):
    """
    Algorithm that returns a list containing Pascal's triangle.

    Args:
        n (int): Specifies the number of rows.

    Returns:
        List: List of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]  # The first element of each row is always 1
        if i > 0:
            prev_row = triangle[i - 1]
            for j in range(len(prev_row) - 1):
                # Calculate the next element by
                # summing up the two elements above it
                next_element = prev_row[j] + prev_row[j + 1]
                row.append(next_element)
            row.append(1)  # The last element of each row is always 1
        triangle.append(row)

    return triangle
