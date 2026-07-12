"""
2520 is the smallest number that can be divided by each of the numbers from
1 to 10 without any remainder.


What is the smallest positive number that is evenly divisible (divisible with
no remainder) by all of the numbers from  1 to 20

"""

# brute-force solution

numbers: list[int] = [x for x in range(1, 20)]


def solve():
    """# n % 1..20 = 0"""
    n = 0

    while True:
        n += 1
        multiples = []
        for i in numbers:
            if n % i == 0:
                multiples.append(i)
                if multiples == numbers:
                    return n
            else:
                multiples.clear()


print(solve())
