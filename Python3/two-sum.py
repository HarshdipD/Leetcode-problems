class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 2:
            return []
        
        hashtable = {}
        for a in range(len(nums)):
            value = nums[a]
            comp = target - value
            if (comp not in hashtable):
                hashtable[value] = a
            else:
                 return [hashtable[comp], a]
