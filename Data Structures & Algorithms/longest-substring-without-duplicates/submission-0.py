class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res

        # res = []
        # for i in range(len(s)-1):
        #     if s[i] != s[i+1] and s[i] not in res:
        #         res.append(s[i])
        # return len(res) 

        