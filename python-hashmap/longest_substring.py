def length_of_longest_substring(s: str) -> int:
    if not s: 
        return 0
    left = 0
    max_val = 0
    freq_counter = {}
    for right in range(len(s)):
        freq_counter[s[right]] = freq_counter.get(s[right], 0) + 1
        while(freq_counter[s[right]] > 1):
            freq_counter[s[left]] -=1
            left +=1
        max_val = max(max_val, right -left+1)
    return max_val
    
    

s = "abba"
print(length_of_longest_substring(s))

def test_empty_string():
    return length_of_longest_substring("") == 0

def test_single_char():
    return length_of_longest_substring(" ") == 1

def test_valid_string():
     return length_of_longest_substring("abcabcbb") == 3

def test_repeated_string():
     return length_of_longest_substring("aaaaaaaaaaaaa") == 1

def test_no_repeat_chars():
    return length_of_longest_substring("abcdefghijkl") == 12