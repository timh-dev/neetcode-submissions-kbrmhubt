class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        l = 0
        r = len(nums) - k 

        max_list = []
        while l <= r:
            max_list.append(max(nums[l:k + l]))
            l += 1

        return max_list