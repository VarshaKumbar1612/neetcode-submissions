class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
        for i, n in enumerate(nums):
            val = target-n

            if val in values:
                return [values[val], i]
            
            values[n] = i
            
        return [] 