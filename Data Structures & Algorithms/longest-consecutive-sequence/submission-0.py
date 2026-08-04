class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        s_nums = sorted(set(nums))
        curr = 1
        long = 1
        for i in range(len(s_nums)-1):
            if s_nums[i+1] == s_nums[i]+1:
                curr+=1
            else:
                curr = 1
            long = max(long, curr)
        return long