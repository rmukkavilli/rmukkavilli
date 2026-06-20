# def move_zeros(nums):
#     left = 0
#     # right = 0
#     # l = len(nums)
#     # while (left < l and right < l):
#     #    if nums[left]==0 and nums[right] !=0:
#     #         temp = nums[left]
#     #         nums[left] = nums[right]
#     #         nums[right] = temp
#     #         left +=1
#     #    right +=1
    
#     for right in range(len(nums)):
#         print(nums[right])
#         if nums[right] != 0:
#             nums[left], nums[right] = nums[right], nums[left]
#         left +=1
#     return nums

def moveZeroes(nums):
    nextNonZero = 0  # Pointer for next non-zero position
    
    for i in range(len(nums)):
        if nums[i] != 0:  # Found non-zero element
            nums[nextNonZero], nums[i] = nums[i], nums[nextNonZero]  # Swap
            nextNonZero += 1  # Move position forward
    
    return nums

# Test
print(moveZeroes([0, 1, 0, 3, 12]))  # Output: [1, 3, 12, 0, 0]
print(moveZeroes([1, 2]))  # Output: [1, 2]
print(moveZeroes([0, 0, 1]))  # Output: [1, 0, 0]