class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
        for x in range(len(nums)-k):
            heapq.heappop(heap)
        return heapq.heappop(heap)