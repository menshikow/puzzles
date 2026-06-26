"""
Given an integer array nums sorted in non-decreasing order
return an array of the squares of each number sorted in non-decreasing order.

non-decreasing order => each number in a sequence is greater than or equal to the previous number.
"""
# Example 1:

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

# Example 2:

# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]

# Constraints:

#     1 <= nums.length <= 104
#     -104 <= nums[i] <= 104
#     nums is sorted in non-decreasing order.

 
# Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?
 

class Solution:
     def sortedSquares(self, nums: list[int]) -> list[int]:
          """
          don't try to do it with 'in-place merging'
          have to create a new array with nulls
          """
          n: int = len(nums)
          result: list[int] = [0] * n

          left: int = 0
          right: int = n - 1

          for i in range(n-1, -1, -1):
               if abs(nums[left]) < abs(nums[right]):
                    result[i] = nums[right] * nums[right]
                    right -= 1
               else:
                    # bucket-sort O(nlogn) vs 2-pointer approach is O(n)
                    result[i] = nums[left] * nums[left]
                    left += 1
          
          return result