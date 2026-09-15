class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        string = set()
        max_len = 0

        for r in range(len(s)):
            while s[r] in string:
                string.remove(s[l])
                l+=1
            string.add(s[r])
            max_len = max(max_len, r-l+1) 
        return max_len 
