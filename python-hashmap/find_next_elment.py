def next_greater_elements(nums: list[int]) -> list[int]:
    stack = []
    res = [-1] * len(nums)
    for i in range(len(nums)):
        while stack and nums[i] > nums[stack[-1]]:
            index = stack.pop()
            res[index] = nums[i]
        stack.append(i)
    return res
    
nums = [2, 1, 2, 4, 3]

print(next_greater_elements(nums))