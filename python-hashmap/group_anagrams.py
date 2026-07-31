# n = number of words
# m = maximum word length
# Time: O(n × m log m)
# Space: O(n × m)
def group_anagrams(words: list[str]) -> list[list[str]]:
    # Your implementation
    group_dict= {}
    for word in words:
        key = "".join(sorted(word))
        if key not in group_dict:
            group_dict[key] = []
        group_dict[key].append(word)
    return list(group_dict.values())


words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(words))