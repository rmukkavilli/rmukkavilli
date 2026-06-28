def longest_substring_replace(s):
    set_str = set()
    left = 0
    max_len = 0
    best_start = 0
    for right in range(len(s)):
        while s[right] in set_str:
            set_str.remove(s[left])
            left +=1
        
        set_str.add(s[right])
        if best_start > max_len:
            max_len = right - left +1
            best_start = left
        max_len = max(max_len, right-left+1)
        print (s[best_start: best_start + max_len])
    return max_len

s = "abcabcbb"
print(longest_substring_replace(s))