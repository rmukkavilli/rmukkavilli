import pytest
def character_replacement(s: str, k: int) -> int:
    freq_char = {}
    left =0
    max_val =0
    max_freq = 0
    if s is None:
        return 0
    if k < 0:
        raise ValueError("k value can not be -ve")
    for right in range(len(s)):
        freq_char[s[right]] = freq_char.get(s[right], 0)+1
        max_freq = max(freq_char[s[right]], max_freq)
        while (right - left + 1) - max_freq > k:
            freq_char[s[left]] -=1
            left +=1

        max_val = max(max_val, right -left +1)
    return max_val
        
s = "ABCDEF"
k = 1
print(character_replacement(s, k))



# Unit test cases"
def test_empty_string():
    assert character_replacement("", 2) == 0


def test_all_repeated():
    assert character_replacement("AA", 2) == 2

def test_single_char():
    assert character_replacement("A", 2) == 1

def test_non_repeated_char():
    assert character_replacement("ABCDEF", 1) == 2

def test_k_val_zero():
    assert character_replacement("ABCC", 0) == 2

def test_negative_k():
    with pytest.raises(ValueError):
        character_replacement("ABCC", -2)