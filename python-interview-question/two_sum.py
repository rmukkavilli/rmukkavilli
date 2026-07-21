# Spnace :O(N) and O(1) and use enumerate.
def two_sum(nums,target):
    index ={}
    i = 0
    for num in nums:
        sum = target - num
        if sum in index:
            return index[sum], i
        else:
            index[num] = i
        i +=1

nums = [4,4,4]
target = 2

print(two_sum(nums, target))