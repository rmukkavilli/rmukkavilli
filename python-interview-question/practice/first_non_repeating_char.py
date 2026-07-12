# Time Complexity: O(2N) -> O(N)
#   Pass 1: Count frequency of each character.
#   Pass 2: Find the first character with frequency == 1.
#
# Space Complexity: O(N)
#   Frequency dictionary stores up to N unique characters.
def first_unique_char(s: str) -> str | None:
    freq_dict = {}

    for ch in s:
        freq_dict[ch] = freq_dict.get(ch, 0) +1

    for ch in s:
        if freq_dict[ch] == 1:
            return ch
    return None
    




#Input:
s = "leetcode"
t = "loveleetcode"
v = "aabbcc"
print(first_unique_char(s))
print(first_unique_char(t))
print(first_unique_char(v))


# Output:
# None

# Output:
# 'l'

#Output:
# 'v'