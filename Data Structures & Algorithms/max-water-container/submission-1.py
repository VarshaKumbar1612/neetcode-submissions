class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # res = 0 
        # for i in range(len(heights)-1):
        #     for j in range(i, len(heights)):
        #         prod = min(heights[i], heights[j])*(j-i)
        #         res = max(res, prod) 
        # return res
        res = 0
        l, r = 0, len(heights)-1
        while l<r:
            area = min(heights[l], heights[r])*(r-l)
            res = max(res, area)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return res
        