import pytest
def daily_temperatures(temperatures: list[int] | None) -> list[int]:
    if not temperatures:
        return []
    stack = []
    res = [0] * len(temperatures)
    for temp in range(len(temperatures)):
       while stack and temperatures[temp] > temperatures[stack[-1]]:
            index = stack.pop()
            res[index] = temp - index
       stack.append(temp)
    return res

temperatures = [73,74,75,71,69,72,76,73]
print(daily_temperatures(temperatures))


# unit test cases : 
def test_empty_list():
    assert daily_temperatures([]) == []

def test_None_as_list():
    assert daily_temperatures(None) == []

def test_single_entry_list():
    assert daily_temperatures([73]) == [0]

def test_single_entry_list():
    assert daily_temperatures([73]) == [0]

def test_negative_values():
    assert daily_temperatures([-73, -74]) == [0, 0]

def test_valid_values():
    assert daily_temperatures([73,74,75,71,69,72,76,73]) == [1, 1, 4, 2, 1, 1, 0, 0]