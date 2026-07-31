from typing import List
import pytest

def findAnagrams(s: str | None, p: str| None) -> List[int]:
    if not isinstance(s, str) or not isinstance(p, str):
        return []

    if len(p) > len(s):
        return []
    if not p or not s:
        return []
    

    s_freq = {}
    p_freq ={}
    window_len = len(p)
    left = 0
    result = []
    for right in range(len(p)):
        p_freq[p[right]] = p_freq.get(p[right], 0)+ 1
    
    for right in range(len(s)):
        s_freq[s[right]] = s_freq.get(s[right], 0)+ 1
        if (right -left +1) > window_len:
            s_freq[s[left]] -=1
            if(s_freq[s[left]]) == 0:
                del s_freq[s[left]]
            left +=1
        if (s_freq == p_freq):
            result.append(left)
    return result

s = "cbaebabacd"
p = "abc"
s1 = "abab"
p1 = "ab"
print(findAnagrams(s, p))

# Unit test cases 

def test_empty_string():
    assert findAnagrams("", "") ==  []

def test_with_None():
    assert findAnagrams(None, None) == []

def test_single_space_string():
    assert findAnagrams(" ", "") == []

def test_single_space_strings():
    assert findAnagrams(" ", " ") == [0]

def test_no_permutations_string():
    assert findAnagrams("ceaebabadd", "abc") == []

def test_with_permutations_string():
    assert findAnagrams("cbaebabacd", "abc") == [0, 6]