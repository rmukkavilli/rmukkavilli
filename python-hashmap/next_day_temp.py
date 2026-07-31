def daily_temperatures(
    temperatures: list[int] | None
) -> list[int]:
    """
    Return how many days you must wait for a warmer temperature.

    If there is no warmer future temperature, return 0 for that day.

    Example:
    [73, 74, 75, 71, 69, 72, 76, 73]
    -> [1, 1, 4, 2, 1, 1, 0, 0]

    []   -> []
    None -> []
    """
    if not temperatures:
        return []
    stack = []
    res = [0] * len(temperatures)
    for i,temp in enumerate(tempartures):
        while stack and temp > temperatures[stack[-1]]:
            prev_index = stack.pop()
            res[prev_index] = i - prev_index
        stack.append(i)
    return res



tempartures = [73, 74, 75, 71, 69, 72, 76, 73]
print(daily_temperatures(tempartures))
            
def test_None_temp():
    assert daily_temperatures(None) == []

def test_empty_list():
    assert daily_temperatures([]) == []

def test_valid_list():
    assert daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
