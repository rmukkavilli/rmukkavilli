def max_consequetive_ones(nums, k):
    max_count = {}
    left = 0
    max_len = 0
    for right in range(len(nums)):
        max_count[nums[right]] = max_count.get(nums[right], 0)+1
        while(max_count.get(0, 0) > k):
            max_count[nums[left]] -=1
            if max_count[nums[left]] == 0:
                del max_count[nums[left]]
            left +=1
        max_len = max(max_len, right - left +1)
    return max_len
    
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(max_consequetive_ones(nums, k))