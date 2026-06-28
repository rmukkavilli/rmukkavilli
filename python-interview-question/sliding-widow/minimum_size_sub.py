def minimum_size_sub(nums,k):
    left =0
    min_window = len(nums) -1
    new_sum = 0
    for right in range(len(nums)):
        new_sum +=nums[right]
        while new_sum >= k:
            print(left, "", right)
            new_sum -=nums[left]
            min_window = min(min_window, (right -left+1))
            nums[left] -=1
            left +=1
    return min_window




nums=[2,3,1,2,4,3]
k = 7
print(minimum_size_sub(nums, k))