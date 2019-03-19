class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        l,r = 0, len(height)-1
        while(l<r):
            width = r-l
            if(height[l]<height[r]):
                min_height = height[l]
                l+=1
            else:
                min_height = height[r]
                r-=1
            maxArea = max(maxArea, min_height*width)
        return maxArea
