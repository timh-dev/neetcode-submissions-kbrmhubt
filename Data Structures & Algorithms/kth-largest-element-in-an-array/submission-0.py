class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        

        for i in range(0, k):
            inx = nums.index(max(nums))
            final = nums.pop(inx)
        return final