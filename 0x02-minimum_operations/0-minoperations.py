#!/usr/bin/python3
"""Minimum Operations"""

def primeFactorization(x):
    """Returns prime factorization elements of x"""
    div = 2
    factors = []
    while div <= x:
        if x % div == 0:
            factors.append(div)
            x /= div
        else:
            div += 1
    return factors

def minOperations(n):
    """Calculates the fewest number of operations needed
        to result in exactly n H characters in the file"""
    total_operations = 0
    factors = primeFactorization(n)
    occurrences = {item: factors.count(item) for item in factors}

    for factor, count in occurrences.items():
        total_operations += factor * count

    return total_operations

