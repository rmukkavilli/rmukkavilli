import pytest
def longest_substring_k_distinct(s: str, k: int) -> int:
    max_val = 0
    freq_dict = {}
    left = 0
    max_len = 0
    if s is None:
        return 0
    if k < 0: 
        raise ValueError("K can not be -ve")
    for right in range(len(s)):
        freq_dict[s[right]] = freq_dict.get(s[right], 0) + 1
        while (len(freq_dict) > k):
            freq_dict[s[left]] -=1
            if freq_dict[s[left]] == 0:
                del freq_dict[s[left]]
            left +=1

        max_val = max(max_val, right -left+1)
    return max_val

s = "ABCD"
k = 1
print(longest_substring_k_distinct(s, 1))



# Unit test case : 

def test_empty_string():
    assert longest_substring_k_distinct("", 1) == 0

def test_distinct_zero():
    assert longest_substring_k_distinct("ABC", 0) == 0

def test_all_distinct_char():
    assert longest_substring_k_distinct("ABCD", 1) == 1

def test_repeated_char():
    assert longest_substring_k_distinct("aabbaabbccddcc", 1) == 2

def test_with_none():
    assert longest_substring_k_distinct(None, 1) == 0

def test_with_k_val_negative():
    with pytest.raises(ValueError):
        longest_substring_k_distinct("abc", -3)
