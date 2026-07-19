def longest_ones(nums: list[int], k: int) -> int:
    result = 0
    zero_counter = 0
    current_sum = 0

    for end in range(len(nums)):
        if nums[end] == 0:
            zero_counter += 1
        current_sum += 1
        if (zero_counter == k):
            result = max(result, current_sum)
            current_sum = 0
    
    return result 
