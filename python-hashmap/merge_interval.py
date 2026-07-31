# Time:  O(n log n)
# Space: O(n)
# ensure sorting and edge cases are imporatatn
def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    # Your implementation
    if len(intervals)== 0:
        return []
    if len(intervals) ==1:
        return intervals
    intervals = sorted(intervals)
    prev_start = intervals[0][0]
    prev_end = intervals[0][1]
    result = []
    for interval in intervals[1:]:
        curr_start = interval[0]
        curr_end = interval[1]
        if curr_start <= prev_end:
            prev_end = max(prev_end, curr_end)
        else:
            result.append([prev_start, prev_end])
            prev_start = curr_start
            prev_end = curr_end
    result.append([prev_start, prev_end])
    return result

#intervals = [[1, 3], [2, 6], [8, 10], [9, 12], [15, 18]]
intervals = [[1,3,5]]
print(merge_intervals(intervals))
# Expected: [[1, 6], [8, 12], [15, 18]]