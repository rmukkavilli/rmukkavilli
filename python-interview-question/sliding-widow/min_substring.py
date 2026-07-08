def min_substring(s, t):
    min_count = float("inf")
    t_count = {}
    s_count = {}
    have = 0
    left = 0

    for ch in t:
        t_count[ch] = t_count.get(ch, 0) + 1

    for right in range(len(s)):
        ch = s[right]
        s_count[ch] = s_count.get(ch, 0) + 1

        if ch in t_count and s_count[ch] == t_count[ch]:
            have += 1

        while have == len(t_count):
            min_count = min(min_count, right - left + 1)

            left_ch = s[left]
            s_count[left_ch] -= 1

            if left_ch in t_count and s_count[left_ch] < t_count[left_ch]:
                have -= 1

            left += 1

    return min_count if min_count != float("inf") else 0

s = "ADOBECODEBANC"
t = "ABC"
print(min_substring(s,t))