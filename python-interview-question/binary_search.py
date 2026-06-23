def binary_search(nums, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    
    if target == nums[mid]:
        return mid
    elif target > nums[mid]:
        return binary_search(nums, target, mid+1, right)
    else:
        return binary_search(nums, target, left, mid-1)

nums = [-1,0,3,5,9,12]
target = 9
left = 0
right = len(nums)-1
print(binary_search(nums, target, left, right))