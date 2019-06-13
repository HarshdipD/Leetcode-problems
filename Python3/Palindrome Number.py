#  This is a simple problem
#  If the numbers are same forward to backward as backward to forward, return true
#  I converted the number to string, then checked the condition, and returned the boolean value

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        return x == x[::-1]
