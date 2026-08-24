class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # if len(nums) <= 1:
        #     return nums[0]
        
        # # res = []
        # max_val = float('-inf')
        # for i in range(len(nums)):
        #     for j in range(i, len(nums)):    ---->brute force solutions
        #         sums = 0
        #         for k in range(i, j+1):
        #             sums += nums[k]
        #         max_val = max(max_val, sums)

        # return max_val 

# ----------------------------------------------------------------
        # if len(nums) <= 1:
        #     return nums[0]
        
        # # res = []
        # max_val = float('-inf')
        # for i in range(len(nums)):
        #     sums = 0
        #     for j in range(i, len(nums)):   ------> better
        #         sums += nums[j]
        #         max_val = max(max_val, sums)

        # return max_val

# --------------------------------------------------------------------

        sums, maxi = 0, float('-inf')
        for i in range(len(nums)):
            sums += nums[i]

            if sums > maxi:
                maxi = sums
            if sums < 0:
                sums = 0
        return maxi


