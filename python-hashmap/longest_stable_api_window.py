def longest_stable_window(
    responses: list[str],
    k: int
) -> int:
    if responses is None or len(responses) == 0:
        return 0
    if k < 0:
        raise ValueError("k must be non-negative")
    count = 0
    left = 0
    max_value = 0
    unstable = {
        "TIMEOUT",
        "RATE_LIMIT",
        "SERVER_ERROR"
    }
    for right in range(len(responses)):
        if responses[right] in unstable:
            count+=1
        while count > k:
            if responses[left] == "TIMEOUT" or responses[left] == "RATE_LIMIT" or responses[left] == "SERVER_ERROR":
                count -=1
            left +=1
        max_value = max(max_value, right - left +1)
    return max_value
            


responses = [
    "SUCCESS",
    "TIMEOUT",
    "SUCCESS",
    "RATE_LIMIT",
    "SUCCESS",
    "SUCCESS",
    "TIMEOUT",
]
print(longest_stable_window(responses, 1))


# unit test cases:
# 1 empty 
def test_empty_list():
    responses = []
    k = 7
    assert longest_stable_window(responses, k) == 0

 # 2 all failure 
def test_all_failures():
    responses = ["TIMEOUT",
    "RATE_LIMIT",
    "TIMEOUT",
    "SERVER_ERROR",
    "TIMEOUT",
    "RATE_LIMIT",
    "TIMEOUT",]
    k = 2
    assert longest_stable_window(responses, k) == 2
    
# 3 all success 
def test_all_errors():
    responses = ["SUCCESS",
    "SUCCESS",
    "SUCCESS",
    "SUCCESS",
    "SUCCESS",
    "SUCCESS",
    "SUCCESS",]
    k = 7
    assert longest_stable_window(responses, k) == 7

# 4 k greater than len of responses 
def test_k_greater_than_len():
    responses = [
    "SUCCESS",
    "TIMEOUT",
    "SUCCESS",
    "RATE_LIMIT",
    "SUCCESS",
    "SUCCESS",
    "TIMEOUT",
]
    k = 10
    assert longest_stable_window(responses, k) == 7
  

def test_invalid_val():
    repsonses = None
    assert longest_stable_window(responses, 2) == 0

import pytest


def test_negative_k():
    with pytest.raises(ValueError):
        longest_stable_window(["SUCCESS"], -1)