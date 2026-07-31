def num_subarrays_min(nums: list[int]):
    stack = []
    res = [1] * len(nums)
    for i, num in enumerate(nums):
        start = i
        while stack and num < stack[-1][1]:
            p_index, p_val = stack.pop()
            left_choices = popped_index - left_boundary
            right_choices = i - popped_index
            start = p_index
        stack.append([start, num])
    return min_val

print(num_subarrays_min([3,2,1,4]))