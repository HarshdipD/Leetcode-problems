# We will use two pass hash table to reduce complexity to O(n)
# we will do two iterations
# (1) add element and index to the hash table
# (2) check if complement (target - nums[i]) exists
# We find that these two iterations can be converted in one, as done below

from collections import Counter

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        c = Counter()
        
        for a in range(0, len(nums)):
            # calculate complement
            complement = target - nums[a]
            
            # if it's in table, and it's not the same index, return the answer
            if (complement in c) and (c[a] != complement):
                return [a, c[complement]]
            
            # otherwise add add the element
            c[nums[a]] = a
        
