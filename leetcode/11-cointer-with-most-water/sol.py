# You are given an integer array height of length n. There are n vertical lines
# drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

"""
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
In this case, the max area of water (blue section) the container can contain is 49.

Example 2:

Input: height = [1,1]
Output: 1

"""


# Time complexity: O()
# Space complexity: O()


def maxArea(beams: list[int]) -> int:
    n: int = len(beams)
    left: int = 0
    right: int = n - 1

    max_area: int = 0
    while left < right:
        x_axis: int = right - left
        y_axis: int = 0

        if beams[left] < beams[right]:
            y_axis = beams[left]
            left += 1
        elif beams[right] < beams[left]:
            y_axis = beams[right]
            right -= 1
        else:
            y_axis = beams[left]
            left += 1

        area = y_axis * x_axis
        max_area = max(max_area, area)

    return max_area


maxArea([1,8,6,2,5,4,8,3,7])