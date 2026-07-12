# TIme complexity : O(N) processsing all intervals.
# Space complexity O(N) storing all intervals
def merge(intervals: list[list[int]]) -> list[list[int]]:
    result = []
    intervals = sorted(intervals)
    prev_start = intervals[0][0]
    prev_end = intervals[0][1]
    for interval in intervals[1:]:
        curr_start = interval[0]
        curr_end = interval[1]
        if curr_start <= prev_end:
            prev_end = max(curr_end, prev_end)
        else:
            result.append([prev_start, prev_end])
            prev_start = curr_start
            prev_end = curr_end
    result.append([prev_start, prev_end])
    return result


interval1 = [[1,3],[2,6],[8,10],[15,18]]
inteval2 = [[1,4],[4,5]]
print(merge(interval1))
print(merge(inteval2))