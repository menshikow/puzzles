"""
Problem 9: Special Pythagorean Triplet

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

There exists exactly one Pythagorean triplet for which a + b + c = 1000
"""

# if a, b, c is a pythogorian triples, then ka, kb, kc for any positive k

# a = m^2 - n^2, b = 2mc, c = m^2 + n^2
# (m^2 - n^2) + (2mn) + (m^2 + n^2) = 1000
# m(m+n)=500
# (500 / m) - m = n

# import random
import math


# note: primitive pythagorian triples vs ka, kb, kc
def euclids_formula(m: int, n: int) -> list[int]:
    """
    for n,m integers, where m > n > 0:
    a = m^2 - n^2, b = 2m, c = m^2 + n^2
    """
    if n == m or n == 0 or m == 0:
        return []

    if math.gcd(m, n) != 1:
        print(f"{m} and {n} are not coprime")
    if n < m:
        n, m = m, n

    a = m**2 - n**2
    b = 2 * m * n
    c = m**2 + n**2

    return [a, b, c]


def test_triple(triple: list[int]) -> bool:
    """
    tets if the triple is a pythogorian triple
    """
    triple = sorted(triple)
    return bool(math.sqrt(triple[0] ** 2 + triple[1] ** 2) == triple[2])


def solve() -> None:
    """
    solving the problem
    """
    # n = random.randint(1, 100)
    # m = random.randint(n + 1, 100)


solve()
