# Time:  O(n)
# Space: O(u)
def first_unique_character(text: str) -> int:
    # Your implementation
    freq_char = {}
    if len(text) == 0:
        return -1
    for ch in text:
        freq_char[ch] = freq_char.get(ch, 0) + 1
    for i, ch in enumerate(text):
        if freq_char[ch] == 1:
            return i
    return -1


tests = [
    ("swiss", 1),
    ("aabb", -1),
    ("", -1),
    ("x", 0),
    ("aabbccd", 6)
]

for text, expected in tests:
    print(text, first_unique_character(text), expected)