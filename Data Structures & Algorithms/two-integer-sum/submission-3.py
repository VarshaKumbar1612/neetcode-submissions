class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            if target-n in seen:
                # return list(i, seen[target-n]) -->list() is used to convert set or tuple or string to list not create a list so u shd first create a tuple (i, seen[target-n]) to use list()
                return [seen[target-n], i]

            seen[n] = i
        return None

        