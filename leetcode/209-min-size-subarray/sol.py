"""
O(n), cause max O(2n) - so O(n)
"""

def min_sub_array_len(target: int, nums: list[int]):
    begin: int = 0
    sum: int = 0
    result = float('inf')

    for end in range(len(nums)):
        sum += nums[end]
        while sum >= target:
            result = min(result, end - begin + 1)
            sum -= nums[begin]
            begin += 1

    if result == float('inf'):
        return 0
    else:
        return result



nums = [2,3,1,2,4,3]
target = 7
print(min_sub_array_len(target, nums))
