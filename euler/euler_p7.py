# problem 7 from project euler: 10001st prime


"""
By listing the first six prime numbers:
2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13

What is the
10.001st prime number?
"""

# brute force factorization approach
# other possibilities: square of n, Sieve of Eratosthenes

n: int = 1
primes: list[int] = []

while len(primes) < 10001:
    n += 1
    divisors: list[int] = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    if len(divisors) == 2:
        primes.append(n)

print(f"primes: {primes}")
