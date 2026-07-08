def insert_interval(intervals, newInterval):
   intervals.append(newInterval)
   intervals = sorted(intervals)
   result = []
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
    
intervals = [[1,2], [3,5], [6,7], [8,10], [12,16]]
newInterval = [4,8]
print(insert_interval(intervals, newInterval))