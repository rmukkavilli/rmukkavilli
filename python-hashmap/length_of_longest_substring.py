def length_of_longest_substring(s: str | None) -> int:
    if s is None:
        return 0
    freq_dict = {}
    left = 0
    max_val = 0
    for right in range(len(s)):
        freq_dict[s[right]] = freq_dict.get(s[right], 0) + 1
        while freq_dict[s[right]] > 1:
            freq_dict[s[left]] -=1
            if freq_dict[s[left]] ==0:
                del freq_dict[s[left]]
            left +=1
        max_val = max(max_val, right -left +1)
    return max_val
        
        

# Input:
s = "abcabcbb"
print(length_of_longest_substring("abba"))

# Output:
# 3

def test_empty_string():
    assert length_of_longest_substring("") == 0


def test_None_string():
    assert length_of_longest_substring(None) == 0


def test_repeated_char():
    assert length_of_longest_substring("abba") == 2

def test_duplicate_all_char():
    assert length_of_longest_substring("bbbb") == 1

def test_no_repeated_char():
    assert length_of_longest_substring("abc") == 3