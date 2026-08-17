class Solution:
    def climbStairs(self, n: int) -> int:
        # dp = {}

        # if n <= 2:
        #     return n

        # if n in dp:
        #     return dp[n]

        # dp[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)

        # return dp[n]
        one, two = 1, 1

        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
        return one