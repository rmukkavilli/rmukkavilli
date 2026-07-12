import re
def word_frequency(text: str) -> dict[str, int]:
    word_freq = {}
    words = re.findall(r"\w+", text.lower())
    for word in words:
        word_freq[word] = word_freq.get(word, 0)+1
    sorted_words =  sorted(word_freq.items(), key=lambda x:x[1], reverse=True)
    print(sorted_words[:2])
    return word_freq


text = "Hello, world! Hello Python. hello"
print(word_frequency(text))

# Output O/P
# {
#     "hello": 3,
#     "world": 1,
#     "python": 1
# }