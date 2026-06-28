

def findAnagrams(s, p):
    if len(p) > len(s):
        return []

    count_p = {}
    window_count = {}
    result = []
    window_len = len(p)

    for ch in p:
        count_p[ch] = count_p.get(ch,0)+1
    
    for right in range(len(s)):
        window_count[s[right]] = window_count.get(s[right], 0)+1
        if right >= window_len:
            left = s[right-window_len]
            window_count[left] -=1
            if window_count[left] == 0:
                del window_count[left]
        if window_count == count_p:
            result.append(right - window_len + 1)
         
    return result


s = "cbaebabacd"
p = "abc"
print(findAnagrams(s,p))