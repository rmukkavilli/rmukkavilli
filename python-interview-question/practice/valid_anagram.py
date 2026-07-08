# time complexity O(n)
# space complexity o(K) k is distinct characters

from collections import Counter
def is_anagram(s: str, t: str) -> bool:
    #return Counter(s) == Counter(t)

    if(len(s) != len(t)):
        return False
    # count each char frequency and just match both s and t
    freq_s = {}
    freq_t = {}
    
    for ch in s:
        freq_s[ch] = freq_s.get(ch, 0) + 1
    for ch in t:
        freq_t[ch] = freq_t.get(ch, 0) + 1
    return freq_s == freq_t



print(is_anagram("anagram", "nagaram"))  # True
print(is_anagram("rat", "car"))          # False
print(is_anagram("ab c", "cab"))         # False