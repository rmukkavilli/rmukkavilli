# fixed window should be first n to k and k to lenth 
def get_average_sum(nums, k):
    window_sum = 0
    max_window_sum =0
    for val in nums[0:k]:
        window_sum +=val
    for val in range(k, len(nums)):
        print(val)
        window_sum += nums[val] - nums[val-k]
        max_window_sum = max(max_window_sum, window_sum)
    return max_window_sum

nums = [1,12,-5,-6,50,3]
nums_1 = [-5,-2,-7,-1]

k = 4
print(get_average_sum(nums, k))