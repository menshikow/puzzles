class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        # 1. Start loop from the last index, going backwards to 0
        # range(start, stop, step) -> start at len-1, stop at -1, step -1
        for i in range(len(digits) - 1, -1, -1):

            # 2. If the digit is less than 9, just add 1 and we are done.
            if digits[i] < 9:
                digits[i] += 1
                return digits

            # 3. If the digit is 9, it becomes 0 (and the loop continues to the next left digit)
            digits[i] = 0

        # 4. If we finished the loop, it means all digits were 9s (e.g., 99 -> 00).
        # We need to insert a 1 at the front (00 -> 100).
        return [1] + digits
