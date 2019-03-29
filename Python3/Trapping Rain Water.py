class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        if height == []: return 0
        total = 0
        left_max, right_max = [None]*len(height), [None]*len(height)
        
        left_max[0] = height[0]
        for a in range(1, len(height)):
            left_max[a] = max(height[a], left_max[a-1])
        
        right_max[len(height)-1] = height[len(height) - 1]
        for a in range(len(height)-2, 0, -1):
            right_max[a] = max(height[a], right_max[a + 1])
        
        for a in range(1, len(height)):
            total += min(left_max[a], right_max[a]) - height[a]
            
        print(left_max, right_max)
        return total
        
