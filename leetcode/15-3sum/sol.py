# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.


# class Solution:
# ass much memory, but why?

# def threeSum(nums: list[int]) -> list[list[int]]:
#     sorted_nums = sorted(nums)
#     i: int = 0
#     sol: list[list[int]] = []

#     while i < len(nums) - 2:
#         k = i + 1
#         j = len(nums) - 1

#         while k < j:
#             result = [sorted_nums[i] + sorted_nums[k] + sorted_nums[j]]
#             if sum(result) == 0:
#                 sol.append(result)
#             elif sum(result) > 0:
#                 j -= 1
#             else:
#                 k += 1
#         i += 1

#     return sol


# test = [-1, 0, 1, 2, -1, -4]
# threeSum(test)


class Solution:
    def threeSum(self, nums:list[int]):
        nums.sort() # O(nlogn)
        result = set()
        n: int = len(nums)

        for i in range(n):
            target: int = -nums[i]
            left: int = i + 1
            right: int = n - 1

            while left < right:
                s: int = nums[left] + nums[right] # cannot add lists to a set
                if s == target:
                    result.add([nums[i], nums[left], nums[right]])
                if s > target:
                    right -= 1
                else:
                    left += 1
        return result