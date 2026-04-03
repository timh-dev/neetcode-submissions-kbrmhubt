class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # solution 1
        #for i in range(0, k):
        #    inx = nums.index(max(nums))
        #    final = nums.pop(inx)
        #return final

        # solution 2
        nums.sort()
        return nums[len(nums) - k]
