def merge_intervels(nums):
    nums = sorted(nums)
    print(nums)
    result= []
    previous_end = nums[0][1]
    previous_start = nums[0][0]
    print(previous_start, ",", previous_end)
    for intervals in nums[1:]:
        curr_start = intervals[0]
        curr_end = intervals[1]
        print(curr_start, "," , curr_end)
        if curr_start <= previous_end:
            previous_end = max(previous_end, curr_end)
        else:
            result.append([previous_start, previous_end])
            previous_start = curr_start
            previous_end = curr_end

    result.append([previous_start, previous_end])
    return result

nums = [[1,3], [2,6], [10,18], [23,50]]
print(merge_intervels(nums))