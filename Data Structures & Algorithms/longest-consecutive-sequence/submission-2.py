class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        s_nums = sorted(set(nums))  # sorted unique list
        longest = 1
        current = 1

        for i in range(1, len(s_nums)):
            if s_nums[i] == s_nums[i-1] + 1:
                current += 1
                longest = max(longest, current)
            else:
                current = 1

        return longest         