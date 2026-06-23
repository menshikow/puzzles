import math


class Solution:
    def sumFourDivisors(self, nums: list[int]) -> int:
        total = 0
        for num in nums:
            divisors: list[int] = []
            for j in range(1, int(math.sqrt(num)) + 1):
                if num % j == 0:
                    divisors.append(j)
                    if j != num // j:
                        divisors.append(num // j)
            if len(divisors) == 4:
                total += sum(divisors)
        return total
