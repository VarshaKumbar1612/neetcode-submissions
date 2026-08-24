from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # freq = Counter(nums)
        # res = []
        # for i in k+1:
        #     res.append(freq[i]) --------> wrong 
        # return res

# ---------------------------------------------------------
        # return  [key for key, val in freq.most_common(k)] 

# ''' freq.most_common(k)
# This gives you the top k elements from the Counter, sorted by frequency.
# Example: if freq = Counter({3:4, 2:3, 1:2, 4:2}) and k=2, then
# freq.most_common(2) → [(3, 4), (2, 3)].'''

# tc = O(n log n)

# ------------------ bucket sorting = tc O(n) -------------------------
        count = {} #is used to track the occurance of each number
        freq = [[] for i in range(len(nums) + 1)]  # the bucket with range len+1

        for num in nums: # fetch elements 
            count[num] = 1 + count.get(num, 0) # update freq count if not then creates it valuing it 0
        for num, cnt in count.items(): 
            freq[cnt].append(num)  # Places num into the bucket list located at index cnt. For example, if number 3 appeared 4 times, it goes into freq[4].

        res = [] 
        for i in range(len(freq) - 1, 0, -1):  # scan from rev in the bucket ro fetch highest val
            for num in freq[i]:  # Loops through all numbers stored inside the bucket at index i.
                res.append(num)  
                if len(res) == k: 
                    return res