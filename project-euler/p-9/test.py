# (m^2 - n^2) + (2mn) + (m^2 + n^2) = 1000

# (15 < m < 23)

import math


def solve():
    for m in range(2, 23):  # m must satisfy m^2 < 500, so m < ~22, padded a bit
        for n in range(1, m):
            if math.gcd(m, n) != 1:
                continue
            if m % 2 == n % 2:  # both odd or both even -> not primitive
                continue

            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n * n
            perimeter = a + b + c

            if perimeter > 1000 or perimeter == 0:
                continue
            if 1000 % perimeter != 0:
                continue

            k = 1000 // perimeter
            a, b, c = a * k, b * k, c * k
            return a, b, c, a * b * c

    return None


print(solve())
