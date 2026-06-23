n1 = 1
n2 = 2
fibs = [1, 2]

def generate_fibonacci(n1: int, n2:int , fibs: list[int]) -> list[int]:
    n1, n2 = n2, n1 + n2

    if n2 > 4_000_000:
        return fibs

    fibs.append(n2)
    return generate_fibonacci(n1, n2, fibs)

fibs = generate_fibonacci(n1, n2, fibs)
print(sum(x for x in fibs if x % 2 == 0))
