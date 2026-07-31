# Sorting: O(n log n)
# Single merge pass: O(n)
# Overall time: O(n log n)
def merge_overlapping_intervals(
    intervals: list[list[int]] | None
) -> list[list[int]]:
    """
    Merge all overlapping intervals.

    Examples:

    [[1, 3], [2, 6], [8, 10], [15, 18]]
    -> [[1, 6], [8, 10], [15, 18]]

    [[1, 4], [4, 5]]
    -> [[1, 5]]

    []
    -> []

    None
    -> []
    """
    if not intervals:
        return []
    intervals = sorted(intervals)
    res = []
    prev_start = intervals[0][0]
    prev_end = intervals[0][1]
    for interval in intervals[1:]:
        curr_start = interval[0]
        curr_end = interval[1]
        if (curr_start <=prev_end):
            prev_end = max(prev_end, curr_end)
        else:
            res.append([prev_start, prev_end])
            prev_start = curr_start
            prev_end = curr_end
    res.append([prev_start, prev_end])
    return res

intervals =  [[1, 3], [2, 6], [8, 10], [15, 18]]
intervals2 = [[1,4],[4,5]]
print(merge_overlapping_intervals(intervals))
print(merge_overlapping_intervals(intervals2))
print(merge_overlapping_intervals([[15, 18], [8, 10], [2, 6], [1, 3]]))


def test_empty_list():
    assert merge_overlapping_intervals([]) == []

def test_list_empty_None():
    assert merge_overlapping_intervals(None) == []

def test_list_non_sorted():
    interval = [[15, 18], [8, 10], [2, 6], [1, 3]]
    assert  merge_overlapping_intervals(interval) == [[1, 6], [8, 10], [15, 18]]