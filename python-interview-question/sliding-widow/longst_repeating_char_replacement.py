# step : 22: 
#1 count {'A': 1}
# 2
# 2 count {'A': 2}
# 1
# 2 count {'A': 2, 'B': 1}
# 3
# 3 count {'A': 3, 'B': 1}
# 2
# 3 count {'A': 3, 'B': 2}
# 3
# 3 count {'A': 2, 'B': 3}
# 2
# 3 count {'A': 2, 'B': 3}

def longest_substring_replace(s, k):
    count =  {}
    max_frequency = 0
    left = 0
    answer = 0
    for right in range(len(s)):
        count[s[right]] = count.get(s[right], 0)+1
        # is only to calculate whats the max frequency number at current window.
        max_frequency = max(count[s[right]], max_frequency)
        # right -left +1 is window size - max_freq ie, 5 - 3 = 2 > k(1)
        while (right - left +1)  - max_frequency > k:
            count[s[left]] -= 1
            left +=1
        answer = max(right - left +1, answer)

    return answer

s = "AABABBA"
k =1
print(longest_substring_replace(s, k))