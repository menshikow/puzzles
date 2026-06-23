from import collections deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        maxsum = -(float("inf"))
        maxlevel = 0

        queue = deque([root])
        level = 1

        while queue:
            size = len(queue)
            s = 0

            for _ in range(size):
                node = queue.popleft()
                s += node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            if s > maxsum:
                maxsum = s
                maxlevel = level

            level += 1

        return maxlevel
