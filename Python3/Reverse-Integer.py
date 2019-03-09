class Solution:
    def reverse(self, x: 'int') -> 'int':        
        res = 0
        while x != 0:
            res = res*10 + x%(-10 if x<0 else 10)
            x = int(x/10)
        
        return 0 if (res < (-2)**31 or res > ((2)**31)-1) else res
