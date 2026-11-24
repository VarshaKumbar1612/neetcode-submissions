class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = {}

        for num in nums:
            # freq[i] = freq.get(i, 0)+1
            freq[num] = freq.get(num, 0) + 1

            if freq[num]>1:
                return True
            
        return False