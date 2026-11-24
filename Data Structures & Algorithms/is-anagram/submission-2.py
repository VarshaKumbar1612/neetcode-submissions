class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_freq = {}
        t_freq = {}
        for val in s:
            s_freq[val] = s_freq.get(val, 0) + 1
        
        for val in t:
            t_freq[val] = t_freq.get(val, 0) + 1
        
        for val in s:
            if s_freq.get(val, 0) != t_freq.get(val, 0):
                return False
        
        return True