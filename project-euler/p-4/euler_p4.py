# def ass() -> list[int]:
#     seq: list[int] = []

#     for a in range(100, 1000):
#         for b in range(a, 1000):
#             # print(f"{a} + {b} = {a * b}")
#             seq.append(a * b)


#     return seq


# def append_pal(seq: list[int]) -> list[int]:
#     pal_seq: list[int] = []

#     for num in seq:
#         if check_palindrome(seq[num]):
#             pal_seq.append(seq[num])

#     return pal_seq


# def solution() -> None:
#     pal_seq = append_pal(ass())

#     print(max(pal_seq))


# solution()


def check_palindrome(n: int) -> bool:
    string_n = str(n)

    left: int = 0
    right: int = len(string_n) - 1

    while left < right:
        if string_n[left] != string_n[right]:
            return False

        left += 1
        right -= 1

    return True


def solution() -> None:
    largest = 0

    for a in range(100, 1000):
        for b in range(a, 1000):
            product = a * b

            if check_palindrome(product) and product > largest:
                largest = product

    print(largest)
