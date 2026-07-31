def check_inclusion(s1: str | None, s2: str | None) -> bool:
    if len(s1) > len(s2):
        return False
    if not s1 or not s2:
        return False
    s1_freq = {}
    s2_freq = {}
    max_val = 0
    window = len(s1)
    left = 0
    for right in range(len(s1)):
        s1_freq[s1[right]] = s1_freq.get(s1[right], 0)+1
    
    for right in range(len(s2)):
        s2_freq[s2[right]] = s2_freq.get(s2[right], 0)+1
        if (right -left +1 > window):
            #left = s2[left] # s2[right - window]
            s2_freq[s2[left]] -=1
            if s2_freq[s2[left]] == 0:
                del s2_freq[s2[left]]
            left +=1
        if s1_freq == s2_freq:
            return True
    return False

s1 = "ab"
s2 = "eidbaooo"
print(check_inclusion(s1, ""))


#Unit test cases

def test_empy_strings():
    assert check_inclusion("", "") == False

def test_single_white_space():
    assert check_inclusion(" ", " ") == True

def test_strings_none():
    assert check_inclusion(None, None) == False

def test_s2_not_matching():
    assert check_inclusion("ab", "eidvaooo") == False

def test_contains_permutation():
    assert check_inclusion("ab", "eidbaooo") is True


def test_does_not_contain_permutation():
    assert check_inclusion("ab", "eidboaoo") is False


def test_repeated_characters():
    assert check_inclusion("aab", "eidbaaooo") is True


def test_s1_longer_than_s2():
    assert check_inclusion("abcd", "abc") is False


def test_none_inputs():
    assert check_inclusion(None, None) is False


def test_empty_strings():
    assert check_inclusion("", "") is False


def test_single_whitespace():
    assert check_inclusion(" ", " ") is True


def test_exact_match():
    assert check_inclusion("abc", "bca") is True


def test_same_length_no_match():
    assert check_inclusion("abc", "abd") is False