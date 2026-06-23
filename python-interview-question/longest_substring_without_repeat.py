def longest_substring(s):
    set_str = set()
    left = 0
    max_len = 0
    for right in range(len(s)):
        while s[right] in set_str:
            set_str.remove(s[left])
            left +=1
        
        set_str.add(s[right])
        max_len = max(max_len, right-left+1)
    print(max_len)

s = "abba"
print(longest_substring(s))