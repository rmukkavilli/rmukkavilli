#Time = O(n * k log k) -
# Space = O(n * k)
def group_anagram(anagrams):
    group = {}
    for anagram in anagrams:
        key = ''.join(sorted(anagram))
        print(key)
        if key not in group:
            group[key] =[]
        group[key].append(anagram)
    return group



anagrams = ["eat","tea","tan","ate","nat","bat"]
print(group_anagram(anagrams))