'''
Novice solutions:
Time-complexity: o(n2)  40ms

class Solution:
    def twoSum(self, nums, target):
        for a in nums:
            for b in nums:
                if(a+b == target):
                    result = [nums.index(a), nums.index(b)]
                    return result
'''

#Time complexity: 

class Solution:
    def twoSum(self, nums, target):
        
