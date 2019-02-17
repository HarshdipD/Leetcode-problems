#Problem - Given an array nums and a value val, remove all instances of that value in-place and return the new length

class Solution:
    def removeElement(self, nums: 'List[int]', val: 'int') -> 'int':
        while val in nums:
            nums.remove(val)
        return len(nums)
