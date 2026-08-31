import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # res = []
        # for i in range(len(nums)):
        #     prd = 1
        #     for j in range(len(nums)):       ------>> O(n^2)
        #         if i != j:
        #             prd *= nums[j]
        #     res.append(prd)
        # return res   

# ----------------------------------------------------------------------------------

        # res = []
        # product = math.prod(nums)
        # for i in range(len(nums)):
        #     if nums[i] != 0:            --------->> if there is a 0 in nums then this will fail 
        #         res.append(product//nums[i]) 
        # return res

# ------------------  prefix sum  -------------------------------------------------

        res = [1] * (len(nums))
        prefix = 1
        # len(nums)
        for i in range(len(nums)):
                res[i] = prefix
                prefix *= nums[i] 
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
                res[i] *= postfix
                postfix *= nums[i]

        return res 






        