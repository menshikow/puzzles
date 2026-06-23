class Solution:
    def maxMatrixSum(self, matrix: list[list[int]]) -> int:
        total_sum = 0
        min_abs_val = float("inf")
        negative_count = 0

        # Iterate through the matrix
        for row in matrix:
            for val in row:
                # Track the sum of absolute values
                total_sum += abs(val)

                # Track smallest absolute value found
                if abs(val) < min_abs_val:
                    min_abs_val = abs(val)

                # Count negatives
                if val < 0:
                    negative_count += 1

        # If even negatives, all can be flipped to positive
        if negative_count % 2 == 0:
            return total_sum

        # If odd negatives, one must remain negative (the smallest one)
        # We subtract 2 * min_abs_val because we added it as positive in total_sum
        else:
            return total_sum - (2 * min_abs_val)


# constrains
# n == matrix.length == matrix[i].length
# 2 <= n <= 250
# -105 <= matrix[i][j] <= 105
