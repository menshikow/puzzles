# bruteforce solution for trying to solve the problem, how many primes are
# there are up to nth number

import math


def check_prime(n: int) -> bool:
    """
    check for 2 until sqrt(n)
    """
    divisors = []
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            divisors.append(i)

    return bool(len(divisors) == 0)


def solve(m: int) -> list[int]:
    """
    solving the problem
    """
    primes: list[int] = []
    n = 1
    while n < m:
        n += 1
        if check_prime(n):
            primes.append(n)

    return primes


print(sum(solve(2000000)))
