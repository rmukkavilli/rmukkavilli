def min_substring(s, t):
    min_count = float("inf")
    t_count = {}
    t_len = len(t)
    have = 0
    left = 0
    count = {}
    for ch in t:
        t_count[ch] = t_count.get(ch, 0)+ 1
   
    for right in range(len(s)):
        count[s[right]] = count.get(s[right], 0)+1
        
        if s[right] in t_count:
            if count[s[right]] == t_count[s[right]]:
                have +=1
        while have == len(t_count):
            min_count = min(min_count, right-left +1)          
            if s[left] in t_count:
               if count[s[left]] == t_count[s[left]]:
                have -=1
            count[s[left]] -=1
            if count[s[left]] == 0:
                del count[s[left]]
#            min_count = min(min_count, right-left +1)
            left +=1
    return min_count


s = "ADOBECODEBANC"
t = "ABC"
print(min_substring(s,t))