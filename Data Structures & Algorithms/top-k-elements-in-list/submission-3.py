from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        # res = []
        # for i in k+1:
        #     res.append(freq[i]) --------> wrong 
        # return res

# ---------------------------------------------------------
        return  [key for key, val in freq.most_common(k)] 

# freq.most_common(k)
# This gives you the top k elements from the Counter, sorted by frequency.
# Example: if freq = Counter({3:4, 2:3, 1:2, 4:2}) and k=2, then
# freq.most_common(2) → [(3, 4), (2, 3)].