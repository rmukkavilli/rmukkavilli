def longest_sequitive(nums):
    #nums_set=set()
    nums_set = set(nums)
    count =0
    longest =0
    for num in nums_set:
        # check num-1 not exist in the list.
        # while loop num+1....and check the max numer iteration.
        if num -1 not in nums_set:
            # Where should count be reset?
            count = 0
            while num+count in nums_set:
                count +=1
        longest = max(count, longest)

    return count
#nums = [100,4,200,1,3,2]
nums = [0,3,7,2,5,8,4,6,0,1]
print(longest_sequitive(nums)) 
