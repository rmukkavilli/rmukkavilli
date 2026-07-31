def longest_substring(s: str) -> int:
    # your code here
    freq_dict = {}
    left = 0
    max_val = 0
    for right in range(len(s)):
        freq_dict[s[right]] = freq_dict.get(s[right],0)+1
        while freq_dict[s[right]] > 1:
            freq_dict[s[left]] -=1
            if freq_dict[s[left]] == 0:
                del freq_dict[s[left]]
            left +=1
        max_val = max(max_val, (right -left +1))
    return max_val



print(longest_substring("abba"))
print(longest_substring("abcabcbb"))
print(longest_substring("abcdef"))
print(longest_substring("bbbbb"))

def test_longest_substring_with_empty_char():
    assert longest_substring("") == 0

def test_longest_substring_with_no_repeated_char():
    assert longest_substring("abcdef") == 6

def test_longest_substring_with_repeated_char():
    assert longest_substring("abcabcbb") == 3

def test_longest_substring_with_valid_char():
    assert longest_substring("pwwkew") == 3

def test_longest_substring_with_all_repeated_char():
    assert longest_substring("bbbbb") == 1