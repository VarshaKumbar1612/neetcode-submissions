from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = Counter(nums)

        for i, val in freq.items():
            if val >= 2:
                return True
        return False