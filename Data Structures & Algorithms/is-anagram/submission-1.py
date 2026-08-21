from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False
        # if sorted(s) == sorted(t):
        #     return True
        # else:
        #     return False     -----> time, space complexity = O(n log n), O(n)

        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t) 
        