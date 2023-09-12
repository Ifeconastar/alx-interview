#!/usr/bin/python3

"""
This script defines a function to determine the winner of
a prime number game played for multiple rounds.
"""


def isWinner(x, nums):
    """
    Determines the winner of each round of the prime number game.

    Args:
        x (int): The number of rounds.
        nums (list of int): An array of n for each round.

    Returns:
        str or None: The name of the player that won the most rounds.
        Returns None if the winner cannot be determined.
    """

    def is_prime(num):
        """
        Checks if a given number is prime.

        Args:
            num (int): The number to check.

        Returns:
            bool: True if the number is prime, False otherwise.
        """
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    def can_win(n):
        """
        Determines if a player can win with a given n.

        Args:
            n (int): The value of n for a round.

        Returns:
            bool: True if the player can win, False otherwise.
        """
        if n == 1:
            return False
        if n % 2 == 0:
            return True
        return False

    def get_winner(n):
        """
        Gets the winner's name based on n.

        Args:
            n (int): The value of n for a round.

        Returns:
            str: The name of the winner ("Maria" or "Ben").
        """
        if n % 2 == 0:
            return "Maria"
        else:
            return "Ben"

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if can_win(n):
            winner = get_winner(n)
            if winner == "Maria":
                maria_wins += 1
            else:
                ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
