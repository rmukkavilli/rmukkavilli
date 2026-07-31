class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not isinstance(s,str) or not isinstance(t,str):
            return None
        if (len(s) < len(t)):
            return None
        
        s_freq = {}
        t_freq = {}
        left = 0
        have = 0
        before_start = 0
        min_val = len(t)
        min_val = float('inf')
        for right in range(len(t)):
            t_freq[t[right]] = t_freq.get(t[right], 0) + 1
        need = len(t_freq)
        
        for right in range(len(s)):
            ch = s[right]
            if ch in t_freq:
                s_freq[ch] = s_freq.get(ch, 0) + 1
                if s_freq[ch] == t_freq[ch]:
                    have +=1          
            while have == need:
                min_val = min(min_val, right - left + 1)
                left_ch = s[left]
                if left_ch in t_freq:
                     s_freq[left_ch] -=1
                     if s_freq[left_ch] < t_freq[left_ch]:
                        have -=1
                     if s_freq[left_ch] == 0:
                        del s_freq[left_ch]
                before_start = left
                left +=1
                
        return s[before_start: before_start +min_val]

s = "ADOBECODEBANC"
t = "ABC"
sol = Solution()
print(sol.minWindow(s,t))