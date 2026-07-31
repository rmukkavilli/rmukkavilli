#
# Your complete mental checklist:

# Calculate mid.
# If nums[mid] == target, return mid.
# Determine the sorted half:
# nums[left] <= nums[mid]
# True → left half is sorted.
# False → right half is sorted.
# If the left half is sorted, check:
# nums[left] <= target < nums[mid]
# True → search left: right = mid - 1
# False → search right: left = mid + 1
# Otherwise, the right half is sorted. Check:
# nums[mid] < target <= nums[right]
# True → search right: left = mid + 1
# False → search left: right = mid - 1

# And yes, the movement rule is always:

# Keep left half  → right = mid - 1
# Keep right half → left = mid + 1

# The boundary directions are intentional:

# Left sorted range:  nums[left] <= target < nums[mid]
# Right sorted range: nums[mid] < target <= nums[right]

# mid is excluded because it was already checked; left or right remains included. Your understanding is

def search_rotated_array(nums: list[int], target: int) -> int:
    # Your implementation
    left = 0 
    right = len(nums) -1
    
    while left <= right:
        mid = (left + right) // 2
      
        if (nums[mid] == target):
            return mid
        # to identify which part is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid -1
            else:
                left = mid+1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid+1
            else:
                right = mid -1
    return -1

          
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
nums1 = [5, 1, 2, 3, 4]
nums2 = [4, 5, 6, 7, 0, 1, 2]
nums3 = []

print(search_rotated_array(nums, target))  # Expected: 4
print(search_rotated_array(nums1 , 4))   # 4
print(search_rotated_array(nums2 , 10)) # -1
print(search_rotated_array(nums3 , 3) )  # -1