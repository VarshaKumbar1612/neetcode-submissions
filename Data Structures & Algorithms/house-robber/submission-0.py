class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # dp = []

        # for i in range(len(nums)-1):
        #     for j in range(i, len(nums)):
        #         if j != (i-1) and j != (i+1) and j!=i:
        #             res = i+j
        #         if res not in dp:
        #             dp.append(res)
        # return max(dp) 
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(n+rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2