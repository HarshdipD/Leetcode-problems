#Fibonacci sequence, but using 1, 1 instead of 0, 1
class Solution:
    def climbStairs(self, n):
        a = b = 1
        for _ in range(n):
            a, b = b, a + b
        return a