class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ''.join(ch.lower() for ch in s if ch.isalnum())
        return new_str == ''.join(reversed(new_str))