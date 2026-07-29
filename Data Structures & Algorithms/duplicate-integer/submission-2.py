from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        if freq and max(freq.values()) >= 2:
            return True
        return False
