import math


def get_prime_factors(n: int ) -> list[int]:
    prime_factors: list[int]= []

    for d in range(2, math.isqrt(n) + 1):
        while n % d == 0:
            prime_factors.append(d)
            n = n // d

    if n > 1:
        prime_factors.append(n)

    return prime_factors

print(get_prime_factors(600851475143))
print(max(get_prime_factors(600851475143)))
