import math


# def get_prime_factors(i: int) -> list:
#     prime_factors = []
#     for d in range(2, math.isqrt(i) + 1):
#         while n % d == 0:
#             prime_factors.append(d)
#             i = i // d 
#     return prime_factors


# def solution(n: int) -> list:
#     multiplies = []

#     factors = get_prime_factors(i)
#     for i in range(1, n + 1):
#         if 3 in factors or 5 in factors:
#             multiplies.append(i)
        
#     return multiplies

# print(solution(1000))

def solution(n):
    multiplies = [i for i in range(1, n) if i % 3 == 0 or i % 5 == 0]
    return sum(multiplies)

print(solution(1000))


