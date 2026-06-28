def longest_substring_with_k_distinct(s, k):
    max_count = {}
    max_len = 0
    left =0
    for right in range(len(s)):
        max_count[s[right]] = max_count.get(s[right], 0)+1
        while(len(max_count) > k):
            max_count[s[left]]-=1
            if max_count[s[left]] == 0:
                del max_count[s[left]]
            left +=1
        max_len = max(max_len, (right - left +1))
    return max_len


s= "eceba"
k =2
print(longest_substring_with_k_distinct(s, k))
