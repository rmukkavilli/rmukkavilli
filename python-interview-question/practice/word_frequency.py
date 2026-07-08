import re
from collections import Counter
def word_frequency(text: str) -> dict[str, int]:
    word_list = re.findall("\w+", text.lower())
    # for word in word_list:
    #     freq[word] = freq.get(word, 0)+1
    return dict(Counter(word_list))
        



text = "Hello, world! Hello world. How are you? Are you okay!!"
print(word_frequency(text))