# idea here is find at each position whether continue old array or start with new 
# At each element, I decide whether to start a new subarray from the current element or extend the previous subarray.
# I keep track of the best sum ending at the current position (current_sum) and the best sum seen so far (max_sum)."
# O(N) and O(1)
#
def max_sum(nums):
    current_sum = nums[0]
    max_sum = nums[0]
    #for num in nums:
    # to start with second elemenet
    for num in nums[1:]:
        current_sum = max(num, current_sum+num)
        max_sum = max(max_sum, current_sum)
    return max_sum
nums = [-2, 1, -3, 4]
# nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_sum(nums))