# TIme complexity : O(N) and Space Complexity : O(N) 
# since we are storing in dict where look up is O(1)
def prefix_sum(nums, k):
    freq_dict = {}
    earlier_sum = 0
    freq_dict[0] = 1
    count = 0
    for num in nums:
        earlier_sum +=num
        needed = earlier_sum - k
        if needed in freq_dict:
            count+=freq_dict[needed]
        freq_dict[earlier_sum] = freq_dict.get(earlier_sum, 0)+1 
    return count
    
#nums = [1, 2, 1, 2, 1]
#nums = [2, 3, -1, 4]
nums = [1, -1, 1]
k = 3#
print(prefix_sum([1, 2, 1, 2, 1],3)) # 4
print("======================")
print(prefix_sum([1,2 -1],2)) # 1
print("======================")
print(prefix_sum([1,-1, 1],1)) # 3
print("======================")
print(prefix_sum([1,1], 2)) # 1
print("======================")
print(prefix_sum([0,0], 0)) # 3