def sliding_window_max(nums:list, k:int) -> list:
    result = []
    window = []
    max_val = 0
    for right in range(len(nums)):
        window.append(nums[right])
        if len(window) == k:
            max_value = window[0]
            for val in window:
                max_value = max(max_value, val)
            result.append(max_value)
            window.pop(0)
    return result

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(sliding_window_max(nums, k))