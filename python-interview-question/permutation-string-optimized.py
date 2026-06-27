def permutations_in_string(s1, s2):
    if (s1 > s2):
        return False
    s1_count = {}
    window_count = {}
    window_size = len(s1)
    for ch in s1:
        s1_count[ch] = s1_count.get(ch, 0)+1
    
    for right in range(len(s2)):
        window_count[s2[right]] = window_count.get(s2[right], 0)+1
        if right >= window_size:
            # perfect move so no need to increment left+=1
            left = s2[right - window_size]
            print(window_count[left])
            window_count[left] -=1
            if window_count[left] ==0:
                del window_count[left]
    return window_count == s1_count
        
        
        

s2 = "adc"
s1 = "cbaebabacd"
print(permutations_in_string(s1, s2))