# Maximum Difference Between Increasing Elements (LeetCode 2016)
# difference between this and max profit is order imporatant
# Time complexity : O(N) since linear all values 
# Space Complexity : O(1) since storing all values in 
def max_difference_increasing_elements(nums) -> int:
    min_value = nums[0]
    max_diff = -1
    for num in nums[1:]:
        if num > min_value:
            max_diff = max(max_diff, num - min_value)
        else:
            min_value = num
    return max_diff

nums = [7, 1, 5, 4]
print(max_difference_increasing_elements(nums))
nums1 = [9, 7, 5, 4, 2]
print(max_difference_increasing_elements(nums1))