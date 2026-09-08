class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(n-1):
            temp = one                     # dp method
            one = one + two
            two = temp
        return one       

        # def fib(n):
        #     if n==0: return 0
        #     if n==1: return 1          # using fib series and recurssion 
        #     else:
        #         return fib(n-1) + fib(n-2)
        
        # return fib(n+1) 

