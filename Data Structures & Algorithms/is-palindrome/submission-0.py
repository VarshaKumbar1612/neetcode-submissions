import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r'[^a-z0-9]','',s)
        length = len(s)
        for i in range(length//2):
            if s[i] != s[length-1-i]:
                return False
        return True