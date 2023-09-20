#!/usr/bin/python3
"""
A function to determine the fewest number of coins
"""


def makeChange(coins, total):
    """Given a pile of coins of completely different values"""
    tmp = 0
    coins.sort(reverse=True)

    if total < 0:
        return 0
    for coin in coins:
        if total % coin <= total:
            temp += total
            total = total % coin

    return tmp if total == 0 else -1
