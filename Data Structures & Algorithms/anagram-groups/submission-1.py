from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1:
            return [strs]

        anagram_map = defaultdict(list)  

        for word in strs:
            key = "".join(sorted(word))
            anagram_map[key].append(word)
        
        return list(anagram_map.values())




        
        
