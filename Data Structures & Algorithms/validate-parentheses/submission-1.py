class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket = {'(':')', '{':'}','[':']'} #hash-maps
        for char in s:
            if char in bracket:
                stack.append(bracket[char]) 
            elif not stack or stack.pop() != char:  # If mismatch or empty stack
                return False

        return not stack
