#!/usr/bin/python3

"""
This script defines a method to calculate
the fewest number of operations needed
to achieve a specific number of characters 'H'
in a text file using Copy All and Paste operations.
"""


def minOperations(n):

    """
    Calculates the minimum number of operations
    needed to achieve 'n' 'H' characters.

    Args:
        n (int): The target number of 'H' characters.

    Returns:
        int: The minimum number of operations required.
        Returns 0 if impossible.
    """
    if n == 1:
        return 0

    def prime_factors(num):

        factors = []
        divisor = 2
        while num > 1:
            while num % divisor == 0:
                factors.append(divisor)
                num //= divisor
            divisor += 1
        return factors

    factors = prime_factors(n)

    if len(factors) == 0:

        return 0

    min_ops = float('inf')
    for factor in factors:
        temp_ops = factor + minOperations(n // factor)
        min_ops = min(min_ops, temp_ops)

    return min_ops
