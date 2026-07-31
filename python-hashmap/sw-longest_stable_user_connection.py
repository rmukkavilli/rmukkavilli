def longest_stable_session(
    events: list[str],
    k: int
) -> int:
    count = 0
    max_val = 0
    left = 0
    if events is None:
        return 0
    if k < 0:
        raise ValueError("k must be non-negative")

    for right in range(len(events)):
        if events[right] == 'ERROR':
            count +=1
            while count > k:
                if events[left] == 'ERROR':
                    count -=1
                left +=1
        max_val = max(max_val, right - left +1)
    return max_val

events = [
    "LOGIN",
    "VIEW",
    "ERROR",
    "VIEW",
    "CLICK",
    "ERROR",
    "LOGOUT"
]
print(longest_stable_session(events,1))

# Unit test cases: 
def test_empty_list():
    assert longest_stable_session([], 1) == 0

def test_list_None():
    assert longest_stable_session(None, 1) == 0

def test_all_error():
    events1 = [
    "ERROR",
    "ERROR",
    "ERROR",
    "ERROR",
    "ERROR"
    ]
    assert longest_stable_session(events1, 1) == 1

def test_no_error():
    events1 = [
    "LOGIN",
    "LOGIN",
    "LOGIN",
    "LOGIN",
    "LOGIN"
    ]
    assert longest_stable_session(events1, 1) == 5

def test_negitive_k():
    with pytest.raises(ValueError):
        longest_stable_window(["SUCCESS"], -1)

