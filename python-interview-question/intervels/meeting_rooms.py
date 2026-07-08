def meeting_rooms(intervals):
    intervals = sorted(intervals)
    prev_start = intervals[0][0]
    prev_end = intervals[0][1]

    for interval in intervals[1:]:
        curr_start = interval[0]
        curr_end = interval[1]
        if curr_start <= prev_end:
            return False
        prev_start = curr_start
        prev_end = curr_end
    return True
intervals = [[0,30], [5,10], [15,20]]
print(meeting_rooms(intervals))