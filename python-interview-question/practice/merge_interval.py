# Time complexity:

# Sorting: O(n log n)

# Merge loop: O(n)
# → Total: O(n log n)

# Space complexity: O(n) for the result list.


def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    merge_list = []
    if not intervals:
        return []
    intervals.sort()
    prev_start = intervals[0][0]
    prev_end = intervals[0][1]
    for interval in intervals[1:]:
        curr_start = interval[0]
        curr_end = interval[1]
        if curr_start <= prev_end:
            prev_end = max(prev_end, curr_end)
        else:
            merge_list.append([prev_start, prev_end])
            prev_start = curr_start
            prev_end = curr_end
    merge_list.append([prev_start, prev_end])
    return merge_list



print(merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))
# -> [[1, 6], [8, 10], [15, 18]]

merge_intervals([[1, 4], [4, 5]])
# -> [[1, 5]]