from collections import Counter


# O(n)
# class Solution:
#     def repeatedNTimes(self, nums: list[int]) -> int:
#         only_nums = set(nums)
#         n = len(set(nums))

#         counts = Counter(nums)

#         for i in only_nums:
#             if counts[i] > 1:
#                 return i


# O(1)
class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        seen = set()
        for i in nums:
            if i in seen:
                return i
            seen.add(i)

        return 0


# You are given an integer array nums with the following properties:
#
# nums.length == 2 * n.
# nums contains n + 1 unique elements.
# Exactly one element of nums is repeated n times.
# Return the element that is repeated n times.
#
#
#
# Example 1:
#
# Input: nums = [1,2,3,3]
# Output: 3
# Example 2:
#
# Input: nums = [2,1,2,5,3,2]
# Output: 2
# Example 3:
#
# Input: nums = [5,1,5,2,5,3,5,4]
# Output: 5
