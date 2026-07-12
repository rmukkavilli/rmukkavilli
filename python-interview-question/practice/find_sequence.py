def find_sequence(nums) -> int:
    num_set = set(nums)
    print(num_set)
    longest = 0
    for num in nums:
        if num-1 not in num_set:
            current_num = num
            count  = 1
            print(current_num, "and", count)
        while current_num+1 in num_set:
            print(current_num+1)
            current_num +=1
            count +=1
            print("count ", count)
        longest = max(longest, count)
    return longest







nums = [1, 2,3,100,9, 4]

#nums = [0,3,7,2,5,8,4,6,0,1]
print(find_sequence(nums))
# Output:
# 9