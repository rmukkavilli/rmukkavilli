import pytest
def longest_stable_session(events: list[str] | None, k: int| None) -> int:
    """
    Return the length of the longest contiguous section containing
    at most k "ERROR" events.

    Examples:
    ["OK", "ERROR", "OK", "OK", "ERROR", "OK"], k=1 -> 4
    [], k=1 -> 0
    None, k=1 -> 0

    Raise ValueError if k < 0.
    """
    if events is None or k is None:
        return 0
    if k < 0:
        raise valueError(f"k value can not be -ve {k}")
    count = 0
    max_count = 0
    left = 0
    for right in range(len(events)):
        if events[right] == "ERROR":
            count+=1
        while (count > k):
            if events[left] == "ERROR":
                count -=1
            left +=1
        max_count = max(max_count, right -left+ 1)
    return max_count

s = ["OK", "ERROR", "OK", "OK", "ERROR", "OK"]
k = 1
print(longest_stable_session(["OK", "ERROR", "OK", "OK", "ERROR", "OK"], 0))

def test_longest_session_with_empty():
    assert longest_stable_session([], 6) == 0

def test_longest_session_with_None():
    assert longest_stable_session(None, 6) == 0

def test_longest_session_with_k_zero():
    assert longest_stable_session(["OK", "ERROR", "OK", "OK", "ERROR", "OK"], 0) == 2

def test_longest_session_with_k_greater_than_list():
    assert longest_stable_session(["OK", "ERROR", "OK", "OK", "ERROR", "OK"], 6) == 6

def test_longest_session_with_all_OK_state():
    assert longest_stable_session(["OK", "OK", "OK", "OK", "OK", "OK"], 6) == 6

def test_with_k_negative():
    with pytest.raises(ValueError):
        longest_stable_session(["OK", "ERROR", "OK", "OK", "ERROR", "OK"], -8)
    
    

